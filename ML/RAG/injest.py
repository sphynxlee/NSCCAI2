# initial a vector database FAISS
# read in and tokenize/embed some textual documentation (pdf format injester)
# store that info in our FAISS DB (lives in a folder)
# setup a "chain" (langchain) user question => grab from DB => prompt => LLM => answer
# use a funky low code solution called Chatlit (Streamlit) to make a chatbot

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


DATA_PATH = "data/"
FAISS_PATH = "vectorstore/"


def load_vector_db():
    loader = DirectoryLoader(DATA_PATH,glob="*.pdf",loader_cls = PyPDFLoader)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    texts = text_splitter.split_documents(data)

    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2', model_kwargs = {'device':'cpu'})

    db = FAISS.from_documents(texts,embeddings)
    db.save_local(FAISS_PATH)



if __name__ == '__main__':
    load_vector_db()

