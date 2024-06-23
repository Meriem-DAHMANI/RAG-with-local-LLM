from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_function():
    #embeddings = BedrockEmbeddings(credentials_profile_name="default", region_name="us-east-1")
    #embeddings = OllamaEmbeddings(model="mistral")
    embeddings = HuggingFaceEmbeddings()

    return embeddings