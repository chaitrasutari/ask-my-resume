# Ask My Resume - Streamlit LLM Application

## 📄 Description
A mini project that lets you interact with your resume PDF using Retrieval-Augmented Generation (RAG) via LangChain.

🔗 **Streamlit App:** [https://chaitrasutari-askmyresume.streamlit.app/](https://chaitrasutari-askmyresume.streamlit.app/)

## 🚀 Features
- Upload a resume (PDF)
- Ask natural language questions ("What are my skills?", "Summarize my experience")
- Built with LangChain, FAISS, HuggingFace Embeddings, and HuggingFace LLMs
- Simple CLI and Streamlit UI


## 🧠 Tech Stack
| Tool               | Purpose                          |
|--------------------|----------------------------------|
| LangChain          | Document parsing, chaining logic |
| HuggingFace        | Embeddings + Free LLM            |
| FAISS              | Vector DB for similarity search  |
| Streamlit          | Simple web UI                    |

## 📁 Project Structure
```
ask-my-resume/
├── app.py              # CLI interface
├── streamlit_app.py    # Streamlit web UI
├── rag_pipeline.py     # RAG pipeline logic
├── config.py           # Paths and model config
├── resume.pdf          # Sample resume for demo
├── requirements.txt    # Dependencies
└── .env                # API keys
```

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/ask-my-resume.git
cd ask-my-resume
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🔑 Setup
Create a `.env` file:
```
HUGGINGFACEHUB_API_TOKEN=hf_...
```
Update `config.py` with your actual PDF path and model if needed.

## 💬 CLI Usage
```bash
python app.py
```
Example:
```
What are my projects?
```

## 🌐 Streamlit UI
### Run it:
```bash
streamlit run streamlit_app.py
```

## Sample Questions
- What are my key skills?
- What frameworks do I know?
- Summarize my experience

## 🚀 Future Scope

- **🕒 Latency Optimization**  
  Current responses from the LLM introduce noticeable delays, especially for large PDFs or complex questions. To improve user experience:
  - Integrate asynchronous processing with background task queues (e.g., `Celery`, `FastAPI + async`)
  - Cache previous responses using Redis or local storage
  - Switch to faster, quantized models or hosted LLMs like `ollama`, `gpt4all`, or use OpenAI with batching

- **📁 Support for Multiple File Types**  
  Extend support beyond PDFs to include DOCX, TXT, or HTML files using LangChain-compatible loaders.

- **📦 Local Embeddings & Models**  
  Reduce dependency on Hugging Face endpoints by serving local models with `Instructor-XL`, `LLaMA`, or `BGE`.

- **📜 Conversational History**  
  Maintain a chat-like experience with full question-answer history, context retention, and follow-ups.

- **🧠 Semantic Chunking Improvements**  
  Replace static chunking with smarter approaches like sentence-aware chunking or semantic segmentation for better QA accuracy.

- **🔒 Authentication & User Isolation**  
  Add user authentication to allow personalized resume uploads, embeddings per user, and private sessions.

## 💼 Why This Project?
> Built to demonstrate hands-on RAG experience using LangChain, and HuggingFace Embeddings.