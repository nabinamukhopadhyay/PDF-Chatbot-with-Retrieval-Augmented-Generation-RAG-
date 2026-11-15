📄 PDF Chatbot with Retrieval-Augmented Generation (RAG)

1. Project Overview

PDF Chatbot with Retrieval-Augmented Generation (RAG) is an AI-powered application that allows users to upload PDF documents and interact with their contents through natural language questions.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-aware responses using a Large Language Model (LLM).

The objective is to provide accurate, document-grounded answers while reducing the chances of AI hallucinations.

2. Key Features

- PDF Upload: Upload PDF documents through an interactive Streamlit interface.
- Text Extraction: Extract text from PDF documents using PyPDFLoader.
- Text Chunking: Split extracted text into smaller chunks for efficient processing.
- Semantic Embeddings: Generate text embeddings using Cohere.
- Vector Database: Store document embeddings using FAISS.
- Contextual Retrieval: Retrieve relevant document chunks using Maximum Marginal Relevance (MMR).
- AI-Powered Responses: Generate answers based on retrieved document context.
- Hallucination Control: Prevent unsupported answers through prompt-based restrictions.
- Chat History: Maintain conversation history during the application session.

3. Technology Stack

Technology| Purpose
Python| Backend development
Streamlit| User interface
LangChain| RAG pipeline
Cohere Embeddings| Semantic embedding generation
FAISS| Vector storage and retrieval
PyPDFLoader| PDF text extraction
RecursiveCharacterTextSplitter| Text chunking
Large Language Model| Answer generation

4. Project Structure

PDF-Chatbot-with-RAG/
│
├── pdf_agent_frontend.py
│
├── pdf_agent_backend.py
│
├── resume_main_logic.py
│
└── resume_checker.py

Note: The two resume-related Python files are separate scripts and are not part of the PDF chatbot workflow.

5. System Architecture and Workflow

The application follows a Retrieval-Augmented Generation pipeline:

1. PDF Upload: The user uploads a PDF through the Streamlit interface.
2. Text Extraction: PyPDFLoader extracts text from the document.
3. Text Chunking: RecursiveCharacterTextSplitter divides the text into chunks of 1,000 characters with an overlap of 200 characters.
4. Embedding Generation: Cohere's "embed-english-v3.0" model converts text chunks into vector representations.
5. Vector Storage: FAISS creates a vector store containing the document embeddings.
6. Information Retrieval: The retriever uses Maximum Marginal Relevance (MMR) to identify relevant document chunks.
7. Answer Generation: The retrieved context is passed to the language model along with the user's question.
8. Response Display: The generated answer is displayed through Streamlit, along with the chat history.

6. RAG Configuration

Parameter| Value
Chunk Size| 1000
Chunk Overlap| 200
Embedding Model| embed-english-v3.0
Vector Store| FAISS
Retrieval Strategy| MMR
Retrieved Documents (k)| 7
Fetch K| 50

7. Installation and Execution

Prerequisites

- Python 3.9 or above
- Cohere API key
- Required Python libraries
- Language model configuration

Step 1: Clone the Repository

git clone https://github.com/nabinamukhopadhyay/PDF-Chatbot-with-Retrieval-Augmented-Generation-RAG.git

Step 2: Navigate to the Project Directory

cd PDF-Chatbot-with-Retrieval-Augmented-Generation-RAG

Step 3: Install Dependencies

Install the required libraries:

pip install streamlit langchain-classic langchain-cohere faiss-cpu pypdf

Step 4: Configure API Credentials

Set your Cohere API key as an environment variable:

export cohere_api_key="YOUR_COHERE_API_KEY"

Configure the language model credentials as required by the model configuration.

Step 5: Run the Application

streamlit run pdf_agent_frontend.py

8. Application Usage

1. Launch the Streamlit application.
2. Upload a PDF document.
3. Wait for the document processing to complete.
4. Enter a question related to the uploaded document.
5. Receive an AI-generated response based on the document.
6. Continue asking questions and review the chat history.

9. Hallucination Control

The application uses explicit prompting instructions to improve response reliability.

- Answers must be based on the retrieved document context.
- The model must not fabricate information.
- If the context is partially relevant but insufficient, the model responds: "I don't know based on the provided context."
- If the context is missing or unrelated, the model responds: "I don't know."
- External facts and unsupported explanations are not permitted.

10. Project Objective

This project demonstrates the practical implementation of Retrieval-Augmented Generation for intelligent document interaction.

By integrating PDF processing, semantic embeddings, vector databases, information retrieval, and Large Language Models, the application provides an interactive approach to extracting information from PDF documents through natural language queries.

---

Technologies: Python | Streamlit | LangChain | Cohere | FAISS | RAG
