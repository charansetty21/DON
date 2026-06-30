from brain.llm import Brain


class ConversationManager:

    def __init__(self):
        self.brain = Brain()

    def process(self, user_text: str) -> str:
        print(f"\nBoss: {user_text}")

        response = self.brain.chat(user_text)

        print(f"DON: {response}")

        return response