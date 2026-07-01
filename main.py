
from brain.planner import execute_intent

def run_don():
    print("=" * 50)
    print("DON AI Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        try:
            user_input = input("You: ").strip()
        except EOFError:
            print("\nDON: Goodbye Boss.")
            break
        except KeyboardInterrupt:
            print("\nDON: Goodbye Boss.")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:
            print("DON: Goodbye Boss.")
            break

        reply = execute_intent(user_input)
        print(f"DON: {reply}")


if __name__ == "__main__":
    run_don()