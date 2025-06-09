# rag_pipeline.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEndpoint

from config import PDF_PATH, MODEL_NAME  

load_dotenv()

def get_qa_chain(pdf_path=PDF_PATH):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(pages, embeddings)

    qa = RetrievalQA.from_chain_type(
        llm = HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            temperature=0.5,
            max_new_tokens=256
        ),
        retriever=db.as_retriever()
    )
    return qa
