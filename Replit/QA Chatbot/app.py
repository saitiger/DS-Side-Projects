import streamlit as st
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
import tempfile
import os

st.set_page_config(page_title='Research Assistant')

def load_pdf(uploaded_file):
    """Loads and splits a PDF file into chunks."""
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

        try:
            loader = PyPDFLoader(temp_file_path)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(documents)
            return texts
        finally:
            os.unlink(temp_file_path)
    return None

def create_vectorstore(texts):
    """Creates a vector store using HuggingFace embeddings."""
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore

def get_llm():
    """Returns a LangChain-compatible HuggingFace model for question-answering."""
    model_name = "deepset/roberta-base-squad2"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)

        hf_pipeline = pipeline(
            "question-answering",
            model=model,
            tokenizer=tokenizer,
        )

        llm = HuggingFacePipeline(pipeline=hf_pipeline)
        return llm
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

def create_qa_chain(vectorstore):
    """Creates a question-answering chain."""
    llm = get_llm()
    if llm is None:
        return None
    
    prompt = PromptTemplate(
        template="""Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:""",
        input_variables=["context", "question"],
    )
    
    try:
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": prompt,
            },
        )
        return qa_chain
    except Exception as e:
        st.error(f"Error creating QA chain: {str(e)}")
        return None

st.title("PDF Summarizer and Q&A")

uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    texts = load_pdf(uploaded_file)
    
    if texts:
        vectorstore = create_vectorstore(texts)
        
        qa_chain = create_qa_chain(vectorstore)

        if qa_chain is not None:
            st.header("Research Assistant")
            user_query = st.text_input("Query :mag:", placeholder="Ask a question about the text...")
            
            if user_query:
                try:
                    st.write("Attempting to answer the question...")
                    response = qa_chain({"query": user_query})
                    st.write(f"**Answer:** {response['result']}")
                except Exception as e:
                    st.error(f"An error occurred while processing the question: {str(e)}")
                    st.error("Please try rephrasing your question or uploading a different PDF.")
        else:
            st.error("Failed to create the QA chain. Please try again or contact support.")
    else:
        st.error("Failed to process the PDF. Please try again with a different file.")
else:
    st.info("Please upload a PDF file to begin.")
