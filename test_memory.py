from brain.memory import ConversationMemory

memory = ConversationMemory(max_messages=3)

memory.add_user_message("Hello")
memory.add_assistant_message("Hi Boss")
memory.add_user_message("Open Chrome")

print(memory.get_history())
print("Length:", len(memory))

memory.add_assistant_message("Opening Chrome...")

print("\nAfter adding another message:")
print(memory.get_history())

memory.clear()

print("\nAfter clear:")
print(memory.get_history())