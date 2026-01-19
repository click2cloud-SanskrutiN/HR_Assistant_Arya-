import sys
from pathlib import Path

from config.settings import settings
from src.agent import (
    load_documents,
    split_documents,
    create_vectorstore
)
from langchain_openai import AzureOpenAIEmbeddings


def main():
    """Ingest documents into vector store"""
    print("\n" + "="*60)
    print("BioPharma SOP Document Ingestion")
    print("="*60 + "\n")
    
    
    try:
        settings.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return
    
   
    if not settings.DOCUMENTS_PATH.exists():
        print(f" Documents folder not found: {settings.DOCUMENTS_PATH}")
        print("\nPlease create folder and add documents:")
        print("  data/documents/SOP-MFG-2024-018_Aseptic_Filling.md")
        print("  data/documents/WI-QC-2024-042_LAL_Endotoxin_Testing.md")
        print("  data/documents/QA-PROC-2024-025_Deviation_CAPA.md")
        return
    
    
    print("STEP 1: Loading documents")
    print("-" * 60)
    documents = load_documents(settings.DOCUMENTS_PATH)
    
    if not documents:
        print(" No documents found")
        return
    
    
    print("STEP 2: Splitting into chunks")
    print("-" * 60)
    chunks = split_documents(documents)
    
    
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        openai_api_version=settings.AZURE_OPENAI_API_VERSION,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_key=settings.AZURE_OPENAI_API_KEY,
    )
    
    
    print("STEP 3: Creating vector store")
    print("-" * 60)
    
    
    import shutil
    vectorstore_path = Path(settings.VECTORSTORE_PATH)
    if vectorstore_path.exists():
        shutil.rmtree(vectorstore_path)
        print("Deleted old vector store")
    
    create_vectorstore(chunks, embeddings)
    
    print("="*60)
    print("✓ Ingestion complete!")
    print("="*60)
    print(f"\nStatistics:")
    print(f"  Documents: {len(documents)}")
    print(f"  Chunks: {len(chunks)}")
    print(f"  Location: {settings.VECTORSTORE_PATH}")
    print(f"\nNow run: python query.py\n")


if __name__ == "__main__":
    main()