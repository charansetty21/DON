class ConversationMemory:
    """
    Stores the recent conversation between the user and DON.
    """

    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self.messages = []

    def add_user_message(self, content):
        self._add_message("user", content)

    def add_assistant_message(self, content):
        self._add_message("assistant", content)

    def _add_message(self, role, content):
        self.messages.append(
            {
                "role": role,
                "content": content
            }
        )

        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_history(self):
        return self.messages.copy()

    def clear(self):
        self.messages.clear()

    def __len__(self):
        return len(self.messages)