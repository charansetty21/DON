from brain.orchestrator import run_don


def main():
    print("=" * 50)
    print("DON AI Assistant (v3 Architecture)")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("DON: Goodbye Boss.")
                break

            response = run_don(user_input)
            print("DON:", response)

        except KeyboardInterrupt:
            print("\nDON: Goodbye Boss.")
            break


if __name__ == "__main__":
    main()