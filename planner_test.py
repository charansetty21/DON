from brain.ai_planner import choose_tool

while True:

    text = input("You: ")

    if text == "exit":
        break

    print()

    print("Planner:", choose_tool(text))

    print()