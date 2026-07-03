from .storage import load_memory, save_memory


class ConversationMemory:
    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self.messages = load_memory()

    def add_user_message(self, content):
        self._add("user", content)

    def add_assistant_message(self, content):
        self._add("assistant", content)

    def _add(self, role, content):
        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

        save_memory(self.messages)

    def get_messages(self):
        return self.messages.copy()

    def clear(self):
        self.messages = []
        save_memory(self.messages)