from brain.ai_planner import plan

while True:
    text = input("You: ")

    if text == "exit":
        break

    print(plan(text))