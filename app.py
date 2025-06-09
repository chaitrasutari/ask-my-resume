# app.py
from rag_pipeline import get_qa_chain
from config import PDF_PATH

def main():
    print("🧠 Ask your resume anything!")
    qa_chain = get_qa_chain(PDF_PATH)

    while True:
        query = input("\nYour question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa_chain.run(query)
        print(f"\n📄 Answer: {answer}")

if __name__ == "__main__":
    main()
