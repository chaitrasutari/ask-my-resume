import streamlit as st
import tempfile
from rag_pipeline import get_qa_chain

st.set_page_config(page_title="📄 Ask About This Document", layout="centered")
st.title("📄 Ask About This Document")

# --- Session state ---
if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False
    st.session_state.tmp_path = None

# --- Reset Button ---
if st.session_state.pdf_uploaded:
    if st.button("🔄 Upload Another Document"):
        st.session_state.pdf_uploaded = False
        st.session_state.tmp_path = None
        st.rerun()  # ✅ full app rerun using modern API

# --- Upload logic ---
if not st.session_state.pdf_uploaded:
    uploaded_file = st.file_uploader("📤 Upload a PDF", type="pdf")
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            st.session_state.tmp_path = tmp_file.name
            st.session_state.pdf_uploaded = True
        st.rerun()  # ✅ re-render to show question prompt only

# --- Question input ---
if st.session_state.pdf_uploaded:
    query = st.text_input("What do you want to know about this document?")
    if query:
        with st.spinner("🔍 Reading and reasoning..."):
            qa_chain = get_qa_chain(st.session_state.tmp_path)
            raw_result = qa_chain.invoke({"query": query})
            answer = raw_result["result"] if isinstance(raw_result, dict) else raw_result
            st.success(answer.strip())
