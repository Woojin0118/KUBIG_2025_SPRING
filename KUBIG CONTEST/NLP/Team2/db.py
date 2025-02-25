from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vectordb = Chroma(
    persist_directory="./wiki_storage",
    embedding_function=embedding_model,
    collection_name="wiki_collection"
)
