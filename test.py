import random

def get_user_question():
    """Prompts the user to ask a question."""
    return input("Ask the Magic 8-Ball a yes/no question: ")

def get_magic_answer():
    """Returns a random response."""
    responses = [
        "It is certain.",
        "Reply hazy, try again.",
        "Don't count on it.",
        "Yes, definitely.",
        "My sources say no."
    ]
    return random.choice(responses)

def main():
    """Main function to run the program."""
    print("--- Welcome to the Python Magic 8-Ball! ---")
    
    # Get the question (we don't actually need to save it to answer it!)
    get_user_question() 
    
    # Get and print the random answer
    answer = get_magic_answer()
    print(f"Magic 8-Ball says: **{answer}**")

# This ensures the program only runs if executed directly
if __name__ == "__main__":
    main()