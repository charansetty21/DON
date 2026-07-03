class MemoryStore:
    """
    Simple in-memory + file-backed memory system for DON.
    """

    def __init__(self):
        self.short_term = []   # session memory
        self.long_term = {}    # persistent key-value memory

    # -------------------------
    # SHORT TERM MEMORY
    # -------------------------
    def add_short(self, item: str):
        self.short_term.append(item)

        # keep last 10 only
        self.short_term = self.short_term[-10:]

    def get_short(self):
        return self.short_term

    # -------------------------
    # LONG TERM MEMORY
    # -------------------------
    def set_long(self, key: str, value):
        self.long_term[key] = value

    def get_long(self, key: str):
        return self.long_term.get(key)

    def get_all_long(self):
        return self.long_term