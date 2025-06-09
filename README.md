# ask-my-resume: Chat with your Resume using RAG + LangChain

## 📄 Description
A mini project that lets you interact with your resume PDF using Retrieval-Augmented Generation (RAG) via LangChain. This is ideal to demonstrate prior experience with LangChain, embeddings, and RAG pipelines — perfect for internships like Prompt Engineering roles.

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

## 🧰 Future Ideas
- Job insights comparison
- Export summaries as PDF/JSON

## 💼 Why This Project?
> Built to demonstrate hands-on RAG experience using LangChain, and HuggingFace Embeddings.