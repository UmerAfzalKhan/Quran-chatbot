import streamlit as st
import os
import sys
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from data_loader import load_quran_data, prepare_documents
from vector_store import create_vector_store
from rag_chain import setup_rag_chain

st.set_page_config(
    page_title="🤖 Quranic Chatbot",
    page_icon="📖",
    layout="wide"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #1A5276;
        font-size: 2.5rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📖 Quranic Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask any Islamic question and get answers from the Quran</p>", unsafe_allow_html=True)

# ==================== CACHE CHECK ====================
@st.cache_resource
def load_quran_resources():
    """Load Quran data and create vector store - CACHED"""
    print("🔄 Loading Quran data (first time only)...")
    surahs = load_quran_data()
    documents = prepare_documents(surahs)
    vectorstore = create_vector_store(documents)
    return surahs, vectorstore

# ==================== LOAD RESOURCES ====================
if 'resources_loaded' not in st.session_state:
    with st.spinner("🔄 Loading Quran data... Please wait (2-3 minutes first time)"):
        try:
            surahs, vectorstore = load_quran_resources()
            st.session_state.surahs_data = surahs
            st.session_state.vectorstore = vectorstore
            st.session_state.resources_loaded = True
            st.success("✅ Quran loaded successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error loading Quran: {str(e)}")
            st.stop()

# ==================== STATS ====================
if 'surahs_data' in st.session_state:
    surahs = st.session_state.surahs_data
    total_ayahs = sum(len(surah.get('ayahs', [])) for surah in surahs)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📖 Surahs", 114)
    with col2:
        st.metric("📜 Ayahs", f"{total_ayahs:,}")
    with col3:
        st.metric("⚡ Status", "Ready")

# ==================== SETUP RAG CHAIN ====================
if 'qa_chain' not in st.session_state and 'vectorstore' in st.session_state:
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        st.warning("⚠️ GROQ_API_KEY not found in .env file")
        api_key = st.text_input("🔑 Enter your Groq API Key:", type="password")
        if api_key and st.button("🚀 Start Chatbot"):
            with st.spinner("Setting up chatbot..."):
                try:
                    st.session_state.qa_chain = setup_rag_chain(
                        st.session_state.vectorstore,
                        api_key
                    )
                    st.success("✅ Chatbot ready!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    else:
        with st.spinner("Setting up chatbot..."):
            try:
                st.session_state.qa_chain = setup_rag_chain(
                    st.session_state.vectorstore,
                    api_key
                )
                st.success("✅ Chatbot ready!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.stop()

# ==================== CHAT INTERFACE ====================
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Assalamu Alaikum! 🌙 I'm here to help you explore the Quran. Ask me any question!"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if 'qa_chain' in st.session_state:
    if prompt := st.chat_input("Ask a question about Quran..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching Quran..."):
                try:
                    response = st.session_state.qa_chain(prompt)
                    answer = response['result']
                    
                    with st.expander("📚 View Quran References"):
                        for doc in response['source_documents']:
                            st.markdown(f"**Surah {doc.metadata['surah']}** - Ayah {doc.metadata['ayah_number']}")
                    
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
else:
    st.info("💡 Please set up the chatbot by providing your Groq API key above.")