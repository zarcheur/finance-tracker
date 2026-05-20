from nlp_parser import parse_expense
from sheety_handler import post_to_sheety

def main():
    print("💰 Welcome to your Finance Tracker!")
    print("Type your transaction in plain English (or 'quit' to exit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye! 👋")
            break

        result = parse_expense(user_input)

        print(f"\n📊 Parsed:")
        print(f"   Amount   : {result['amount']}")
        print(f"   Type     : {result['type']}")
        print(f"   Category : {result['category']}")
        print(f"   Date     : today")

        confirm = input("\nLog this to your sheet? (y/n): ")

        if confirm.lower() == "y":
            post_to_sheety(result)
        else:
            print("Skipped! Try rephrasing.\n")

if __name__ == "__main__":
    main()