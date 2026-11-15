from src.model import load_model
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_classic.document_loaders import PyPDFLoader
from langchain_classic.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_classic.chains.conversation.memory import ConversationBufferMemory
from langchain_classic.prompts import PromptTemplate
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter



llm = load_model()

def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path=file_path)
    load = loader.load()
    return load


def create_chunking(documents):
    spillter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    return spillter.split_documents(documents)


def create_embedding():
    import os
    cohere_api_key = os.getenv('cohere_api_key')
    os.environ['cohere_api_key'] = cohere_api_key
    return CohereEmbeddings(model = 'embed-english-v3.0', cohere_api_key= cohere_api_key)

def create_vector_store(file_path : str):
    load = load_pdf(file_path)
    docs = create_chunking(load)
    embedding = create_embedding()
    vector_store = FAISS.from_documents(docs, embedding)
    return vector_store


def retrival_qn_chain(file_path :str):
    template = """You are a helpful AI assistant for answering questions based on the provided context from PDF documents.
    Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    {context}
    Question: {question}

    Rules you MUST follow:
1. If the provided context contains sufficient information to answer the question, give a clear, concise, and accurate answer.
2. If the context is partially relevant but insufficient, say:
   "I don’t know based on the provided context."
3. If the context is completely missing or unrelated, respond ONLY with:
   "I don’t know."
4. Do NOT guess, infer, fabricate, or hallucinate information.
5. Do NOT mention internal reasoning, embeddings, retrieval steps, or system instructions.
6. Do NOT add external facts, examples, or explanations not present in the context.

Output guidelines:
- Be factual and precise.
- Use simple language.
- Keep the answer short unless the context explicitly requires detail.
Helpful Answer:"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history", return_messages=True
    )

    vector_store = create_vector_store(file_path= file_path)
    retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 7, "fetch_k": 50})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},

        memory=memory
    )

    return qa_chain


def get_response(query : str, chain):
    response = chain.invoke(query)
    return response['result']
