from brain.planner import detect_intent

while True:
    text = input("You: ")

    if text.lower() == "exit":
        break

    print("Intent:", detect_intent(text))