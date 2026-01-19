"""
Streamlit Web Interface for BioPharma SOP Assistant
"""
import streamlit as st
import sys
from pathlib import Path
import traceback

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.agent import SOPAgent
from config.settings import settings

# Page configuration
st.set_page_config(
    page_title="PT Bio Farma SOP Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .source-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
    }
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    try:
        with st.spinner("🔄 Initializing SOP Assistant..."):
            st.session_state.agent = SOPAgent()
            st.session_state.initialized = True
            st.session_state.init_message = "✅ Agent initialized successfully!"
    except FileNotFoundError as e:
        st.error(f"❌ Vector store not found!")
        st.info("📝 Please run: `python ingest.py` first to load documents")
        st.session_state.initialized = False
        st.stop()
    except Exception as e:
        st.error(f"❌ Error initializing agent: {str(e)}")
        with st.expander("🔍 See error details"):
            st.code(traceback.format_exc())
        st.session_state.initialized = False
        st.stop()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'current_sources' not in st.session_state:
    st.session_state.current_sources = []

# Header
st.markdown('<h1 class="main-header">🔬 PT Bio Farma SOP Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ask questions about SOPs, Work Instructions, and Quality Documents</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📚 About")
    
    st.markdown("""
    This AI assistant helps you find information from PT Bio Farma's official documents:
    
    **Available Documents:**
    - 📄 SOP-MFG-2024-018: Aseptic Filling Operations
    - 📄 WI-QC-2024-042: LAL Endotoxin Testing
    - 📄 QA-PROC-2024-025: Deviation & CAPA Management
    """)
    
    st.divider()
    
    st.header("💡 Example Questions")
    
    example_questions = [
        "What is the temperature for aseptic filling?",
        "How do I perform LAL endotoxin testing?",
        "What are the gowning requirements for Grade A?",
        "What is the timeline for investigating a major deviation?",
        "How do I handle a vial breakage during filling?",
        "What are the differential pressure requirements?",
        "What is the acceptance criteria for endotoxin testing?",
        "What is the procedure for CAPA implementation?"
    ]
    
    for i, example in enumerate(example_questions):
        if st.button(example, key=f"example_{i}", use_container_width=True):
            # Store the example question
            st.session_state.example_question = example
            st.rerun()
    
    st.divider()
    
    # Settings
    st.header("⚙️ Settings")
    show_sources = st.checkbox("Show sources", value=True)
    verbose_mode = st.checkbox("Verbose mode (debug)", value=False)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.current_sources = []
        if 'example_question' in st.session_state:
            del st.session_state.example_question
        st.rerun()
    
    # Statistics
    st.divider()
    st.header("📊 Statistics")
    st.metric("Total Questions", len([m for m in st.session_state.chat_history if m["role"] == "user"]))
    st.metric("Model", settings.AZURE_OPENAI_DEPLOYMENT_NAME)

# Main chat interface
st.divider()

# Show initialization message if just started
if 'init_message' in st.session_state and len(st.session_state.chat_history) == 0:
    st.success(st.session_state.init_message)
    del st.session_state.init_message

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Show sources for assistant messages
        if message["role"] == "assistant" and "sources" in message and show_sources:
            if message["sources"]:
                with st.expander("📚 View Sources", expanded=False):
                    for source in message["sources"]:
                        st.markdown(f"""
                        <div class="source-box">
                            <strong>{source['doc_type']}</strong><br>
                            <strong>ID:</strong> {source['document_id']}<br>
                            <strong>Title:</strong> {source['title']}
                        </div>
                        """, unsafe_allow_html=True)

# Handle example question from sidebar
prompt_input = None
if 'example_question' in st.session_state:
    prompt_input = st.session_state.example_question
    del st.session_state.example_question

# Chat input
user_input = st.chat_input("Ask a question about SOPs...")

# Process input (either from chat input or example button)
if user_input or prompt_input:
    actual_input = prompt_input if prompt_input else user_input
    
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": actual_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(actual_input)
    
    # Generate response
    with st.chat_message("assistant"):
        try:
            # Show spinner while processing
            with st.spinner("🔍 Searching documents..."):
                result = st.session_state.agent.query(actual_input, verbose=verbose_mode)
            
            # Display answer
            st.markdown(result["answer"])
            
            # Store and display sources
            if result["sources"] and show_sources:
                with st.expander("📚 View Sources", expanded=False):
                    for source in result["sources"]:
                        st.markdown(f"""
                        <div class="source-box">
                            <strong>{source['doc_type']}</strong><br>
                            <strong>ID:</strong> {source['document_id']}<br>
                            <strong>Title:</strong> {source['title']}
                        </div>
                        """, unsafe_allow_html=True)
            
            # Add to chat history
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": result["answer"],
                "sources": result["sources"]
            })
            
            # Show metadata in verbose mode
            if verbose_mode:
                st.info(f"ℹ️ Retrieved {result['chunks']} relevant chunks")
            
        except Exception as e:
            error_msg = f"❌ Error generating response: {str(e)}"
            st.error(error_msg)
            
            # Show detailed error in expander
            with st.expander("🔍 See error details"):
                st.code(traceback.format_exc())
            
            # Add error to chat history
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": error_msg,
                "sources": []
            })

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9rem;'>
    <p>PT Bio Farma SOP Assistant | Powered by Azure OpenAI</p>
    <p>⚠️ Always verify critical information with official documentation</p>
</div>
""", unsafe_allow_html=True)