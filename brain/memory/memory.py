from brain.memory.memory_store import MemoryStore

memory = MemoryStore()
from brain.memory.memory_store import MemoryStore
from brain.memory.rag.rag_memory import RAGMemory


class MemorySystem:
    def __init__(self):
        self.basic = MemoryStore()
        self.rag = RAGMemory()


memory = MemorySystem()