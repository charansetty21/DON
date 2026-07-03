import numpy as np


class VectorStore:
    def __init__(self):
        self.vectors = []  # list of (embedding, text)

    def add(self, embedding, text):
        self.vectors.append((embedding, text))

    def cosine_similarity(self, a, b):
        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query_embedding, top_k=3):
        scored = []

        for emb, text in self.vectors:
            score = self.cosine_similarity(query_embedding, emb)
            scored.append((score, text))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [text for _, text in scored[:top_k]]