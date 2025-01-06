# Lithuanian Language Learning Bot
# This bot helps users learn basic Lithuanian phrases by providing translations and a fun quiz mode to make the learning more engaging.
# Created by Abraham Kabir, showcasing programming skills and interest in Lithuanian culture.

import random  # Importing random module for selecting random phrases in the quiz


# A dictionary containing English phrases and their Lithuanian translations
phrases = {
    "hello": "labas",
    "goodbye": "viso gero",
    "thank you": "ačiū",
    "please": "prašau",
    "yes": "taip",
    "no": "ne",
    "good morning": "labas rytas",
    "good night": "labanakt",
    "how are you?": "kaip sekasi?",
    "I'm fine, thank you.": "Man sekasi gerai, ačiū.",
    "excuse me": "atsiprašau",
    "I'm sorry": "atsiprašau",
    "where is...?": "kur yra...?",
    "what is your name?": "koks tavo vardas?",
    "my name is...": "mano vardas yra..."
}


def main():
    """
    Main function: Controls the bot's flow, handles user input, 
    and responds with translations, quiz mode or exits the program.
    """
    # Greeting the user and providing instructions
    print("\n\nWelcome to the Lithuanian Language Learning Bot!")
    print("Type 'quit' anytime to exit.\n")
    print("Here are some commands you can use:")
    print("- Type 'quiz' to test yourself.")
    print("- Type an English word/phrase to see the Lithuanian translation.")
    print("- Type a Lithuanian word/phrase to get the English translation.\n")
    
    while True:  # Infinite loop to keep the bot running until the user types quit
        try:
            user_input = input("You: ").strip().lower()  # Getting user input, stripping extra spaces, and converting to lowercase
            
            if user_input == "quit":  # Checks if the user wants to quit
                print("Goodbye! Ačiū!")  # Says goodbye in both English and Lithuanian
                break  # Exits the loop and stop the bot
            
            elif user_input == "quiz":  # If the user wants to play the quiz
                quiz_mode()  # Call the quiz_mode function
            
            elif user_input in phrases:  # If the input matches an English phrase
                print(f"Lithuanian: {phrases[user_input]}")  # Prints the Lithuanian translation
            
            elif user_input in phrases.values():  # If the input matches a Lithuanian phrase
                # Find the corresponding English phrase
                english_word = list(phrases.keys())[list(phrases.values()).index(user_input)]
                print(f"English: {english_word}")  # Print the English translation
            
            else:  # If the bot doesn't recognize the input
                print("Sorry, I don't know that phrase yet. Try another or use 'quiz' mode!")
        
        except KeyboardInterrupt:  # Graceful exits if the user presses Ctrl+C
            print("\nGoodbye! Ačiū!")
            break


def quiz_mode():
    """
    Quiz mode: Tests the user's knowledge by asking them to translate English phrases into Lithuanian.
    """
    print("\nQuiz Mode! Translate the following phrases:")
    
    correct = 0  # Counter for correct answers that increments with each correct answer
    total = 5  # Number of questions in the quiz

    # Randomly select 5 phrases for the quiz
    quiz_phrases = random.sample(list(phrases.items()), total)
    
    for eng, lith in quiz_phrases:  # Loop through the selected phrases
        print(f"Translate this to Lithuanian: '{eng}'")  # Show the English phrase to translate
        answer = input("Your Answer: ").strip().lower()  # Get the user's answer
        
        if answer == lith:  # Check if the answer is correct
            print("Correct! 😊")  # Positive feedback
            correct += 1  # Increment the correct answer count
        else:  # If the answer is wrong
            print(f"Wrong. The correct answer is: {lith}")  # Show the correct answer
    
    # Show the user's quiz results
    print(f"\nQuiz Complete! You got {correct}/{total} correct.")
    print("Keep practicing! 😊\n")


# Entry point of the program
if __name__ == "__main__":
    main()  # Start the bot
