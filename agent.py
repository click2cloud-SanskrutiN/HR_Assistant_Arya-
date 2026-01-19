
import re
from pathlib import Path
from typing import List, Dict

from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage

from config.settings import settings
from src.prompts import SYSTEM_PROMPT, RESPONSE_TEMPLATE


class SOPAgent:
    """BioPharma SOP Question-Answering Agent"""
    
    def __init__(self):
        """Initialize agent with LLM and vector store"""
        print("Initializing SOP Agent...")
        
       
        self.llm = AzureChatOpenAI(
            azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT_NAME,
            openai_api_version=settings.AZURE_OPENAI_API_VERSION,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
            timeout=60,
            max_retries=2,
        )
        
      
        self.embeddings = AzureOpenAIEmbeddings(
            azure_deployment=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
            openai_api_version=settings.AZURE_OPENAI_API_VERSION,
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
        )
        
       
        self.vectorstore = self._load_vectorstore()
        print("Agent initialized\n")
    
    def _load_vectorstore(self) -> FAISS:
        """Load existing FAISS vector store"""
        vectorstore_path = Path(settings.VECTORSTORE_PATH)
        
        if not vectorstore_path.exists():
            raise FileNotFoundError(
                f"Vector store not found at {vectorstore_path}\n"
                f"Please run: python ingest.py"
            )
        
        return FAISS.load_local(
            str(vectorstore_path),
            self.embeddings,
            allow_dangerous_deserialization=True
        )
    
    def query(self, question: str, verbose: bool = False) -> Dict:
        """Answer a question about SOPs"""
        if verbose:
            print(f"\n{'='*60}")
            print(f"Question: {question}")
            print(f"{'='*60}\n")
        
     
        if verbose:
            print("Retrieving relevant documents...")
        
        docs_with_scores = self.vectorstore.similarity_search_with_score(
            question, 
            k=settings.TOP_K
        )
        
        if verbose:
            print(f"Found {len(docs_with_scores)} relevant chunks:\n")
            for i, (doc, score) in enumerate(docs_with_scores, 1):
                doc_id = doc.metadata.get('document_id', 'Unknown')
                title = doc.metadata.get('title', 'Unknown')
                print(f"  {i}. {doc_id} - {title} (Score: {score:.4f})")
            print()
        
        if not docs_with_scores:
            return {
                "answer": f"No relevant information found for: {question}",
                "sources": [],
                "chunks": 0
            }
        
       
        docs = [doc for doc, score in docs_with_scores]
        context = self._format_context(docs)
        
      
        if verbose:
            print("Generating answer...\n")
        
        answer = self._generate_answer(question, context)
        sources = self._extract_sources(docs)
        
        return {
            "answer": answer,
            "sources": sources,
            "chunks": len(docs)
        }
    
    def _format_context(self, docs: List[Document]) -> str:
        """Format documents as context"""
        context_parts = []
        
        for i, doc in enumerate(docs, 1):
            doc_id = doc.metadata.get('document_id', 'Unknown')
            title = doc.metadata.get('title', 'Unknown')
            
            context_parts.append(f"""
[Source {i}: {doc_id}]
{title}

{doc.page_content}

---""")
        
        return "\n".join(context_parts)
    
    def _generate_answer(self, question: str, context: str) -> str:
        """Generate answer using LLM"""
        prompt = RESPONSE_TEMPLATE.format(
            context=context,
            query=question
        )
        
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        return response.content
    
    def _extract_sources(self, docs: List[Document]) -> List[Dict]:
        """Extract source metadata"""
        sources = []
        seen = set()
        
        for doc in docs:
            doc_id = doc.metadata.get('document_id', 'Unknown')
            if doc_id not in seen:
                sources.append({
                    'document_id': doc_id,
                    'title': doc.metadata.get('title', 'Unknown'),
                    'doc_type': doc.metadata.get('doc_type', 'Document'),
                    'filename': doc.metadata.get('filename', 'Unknown')
                })
                seen.add(doc_id)
        
        return sources
    
    def chat(self):
        """Interactive chat mode"""
        print("\n" + "="*60)
        print("PT Bio Farma SOP Assistant - Interactive Mode")
        print("="*60)
        print("Ask questions about SOPs, Work Instructions, and QA documents.")
        print("Type 'exit' to quit, 'help' for tips.\n")
        
        while True:
            try:
                question = input("You: ").strip()
                
                if not question:
                    continue
                
                if question.lower() in ['exit', 'quit', 'q']:
                    print("\nGoodbye!")
                    break
                
                if question.lower() == 'help':
                    self._print_help()
                    continue
                
                
                result = self.query(question)
                print(f"\nAssistant: {result['answer']}\n")
         
                if result['sources']:
                    print("📚 Sources:")
                    for src in result['sources']:
                        print(f"  - {src['doc_type']} {src['document_id']}: {src['title']}")
                    print()
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")
    
    def _print_help(self):
        """Print help"""
        print("""
Example Questions:

1. "What is the temperature requirement for aseptic filling?"
2. "How do I perform LAL endotoxin testing?"
3. "What are the steps for gowning in Grade A area?"
4. "What is the timeline for investigating a major deviation?"
5. "How do I handle a vial breakage during filling?"
6. "What are the acceptance criteria for endotoxin testing?"
7. "What is the differential pressure requirement for Grade A?"

Tips:
- Be specific about what you're asking
- Mention equipment, procedures, or document types if known
- Ask one question at a time
""")



def load_documents(documents_path: Path) -> List[Document]:
    """Load markdown documents"""
    documents = []
    md_files = list(documents_path.glob("*.md"))
    
    print(f"Loading {len(md_files)} documents...")
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = extract_metadata(content, md_file)
            
            doc = Document(
                page_content=content,
                metadata=metadata
            )
            
            documents.append(doc)
            print(f"  ✓ {md_file.name}")
            
        except Exception as e:
            print(f"  ✗ Error loading {md_file.name}: {e}")
    
    print(f"Loaded {len(documents)} documents\n")
    return documents


def extract_metadata(content: str, file_path: Path) -> Dict:
    """Extract metadata from document"""
    metadata = {
        "source": str(file_path),
        "filename": file_path.name
    }
    
    
    doc_id_match = re.search(r'Document ID:\s*([\w-]+)', content)
    if doc_id_match:
        metadata["document_id"] = doc_id_match.group(1)
    
   
    title_match = re.search(r'Title:\s*(.+)', content)
    if title_match:
        metadata["title"] = title_match.group(1).strip()
    
    
    version_match = re.search(r'Version:\s*([\d.]+)', content)
    if version_match:
        metadata["version"] = version_match.group(1)
    
    
    if "SOP" in metadata.get("document_id", ""):
        metadata["doc_type"] = "Standard Operating Procedure"
    elif "WI" in metadata.get("document_id", ""):
        metadata["doc_type"] = "Work Instruction"
    elif "QA" in metadata.get("document_id", ""):
        metadata["doc_type"] = "Quality Assurance Document"
    else:
        metadata["doc_type"] = "Document"
    
    return metadata


def split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into chunks"""
    print(f"Splitting documents into chunks...")
    print(f"Chunk size: {settings.CHUNK_SIZE} | Overlap: {settings.CHUNK_OVERLAP}")
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP,
        separators=[
            "\n================================================================================\n",
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            " ",
            ""
        ],
    )
    
    chunks = splitter.split_documents(documents)
    
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
    
    print(f"Created {len(chunks)} chunks\n")
    return chunks


def create_vectorstore(chunks: List[Document], embeddings) -> FAISS:
    """Create FAISS vector store"""
    vectorstore_path = Path(settings.VECTORSTORE_PATH)
    vectorstore_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Creating FAISS vector store at: {vectorstore_path}")
    print(f"Embedding {len(chunks)} chunks...")
    
   
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )
    
   
    vectorstore.save_local(str(vectorstore_path))
    
    print("Vector store created\n")
    return vectorstore