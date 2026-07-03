from brain.memory.rag.embeddings import EmbeddingModel
from brain.memory.rag.vector_store import VectorStore


class RAGMemory:
    def __init__(self):
        self.embedder = EmbeddingModel()
        self.store = VectorStore()

    def add(self, text: str):
        embedding = self.embedder.embed(text)
        self.store.add(embedding, text)

    def search(self, query: str):
        query_embedding = self.embedder.embed(query)
        return self.store.search(query_embedding)