# Dictionary key: is the question and answer
# Start Function
# get_random_question
# show_question
# show_answer
# Quit_app
import random

flashcards = [
    {"what Python keyword is used to define a function?" : "", "answer" : "def"},
    {"question" : "What data type represent whole numbers?", "answer" : "int"},
    {"question" : "i want to be?", "answer" : "artist"},
]

'''
Task: Tell the user goodbye.
Input: None
Side effect: Prints a goodbye message to Terminal
Return: None
'''

def Quit_app():
    print("Thanks for studying")


'''
Task: Selects and Retrieves a Random Elements in the Flashcards list
Input: Flashcard list
Side effect: None
Return: the Flashcards (dictionary)
'''

def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card


'''
Task: Display the question
Input: Question Card
Side effect: Print the question Text to Terminal
Return: None
'''

def show_question(cards):
    question = card["question"]
    print("Question:", question)

'''
Task: Display the answer
Input: Answer Card
Side effect: Print the answer Text to Terminal
Return: None
'''

def show_answer(cards):
    answer = answer["answer"]
    print("Answer:", answer)

def main():

    while true:
        card = get_random_questions(flashcards)
        show_question(card)

user_choice = input("Enter Q to quit, type anything else to continue: ").lower().strip()

    if choice == "q":
        Quit_app()
          break
    
    else:
        show_answer(card)

main()

