import random
import time

def get_vader_response():
    quotes = [
        "I find your lack of faith disturbing.",
        "The Force is strong with this one.",
        "I am altering the deal. Pray I don't alter it any further.",
        "You have failed me for the last time.",
        "If you only knew the power of the dark side.",
        "I am your father.",
        "Impressive. Most impressive.",
        "You don't know the power of the dark side!",
        "When I left you, I was but the learner; now I am the master.",
        "Give yourself to the dark side. It is the only way you can save your friends.",
        "The Emperor is not as forgiving as I am.",
        "You are beaten. It is useless to resist.",
        "All too easy.",
        "I have you now.",
        "You underestimate the power of the dark side.",
        "Your destiny lies with me, Skywalker. Obi-Wan knew this to be true.",
        "The ability to destroy a planet is insignificant next to the power of the Force.",
        "You have learned much, young one.",
        "Don't make me destroy you.",
        "I see through the lies of the Jedi.",
        "It is pointless to resist, my son.",
        "There is no escape. Don't make me destroy you.",
        "You do not yet realize your importance.",
        "Indeed, you are powerful as the Emperor has foreseen.",
        "No, I am your father.",
        "Your thoughts betray you.",
        "I sense something, a presence I've not felt since...",
        "I have felt it.",
        "This will be a day long remembered.",
        "You have controlled your fear. Now, release your anger.",
        "I hope so, Commander, for your sake. The Emperor is not as forgiving as I am.",
        "There is no conflict.",
        "We meet again at last. The circle is now complete.",
        "Don't underestimate the Force.",
        "I see you have constructed a new lightsaber. Your skills are complete.",
        "You should not have come back.",
        "We would be honored if you would join us.",
        "You have controlled your fear. Now, release your anger. Only your hatred can destroy me.",
        "If he could be turned, he would become a powerful ally.",
        "He will join us or die, master.",
        "Search your feelings. You know it to be true."
    ]
    return quotes[random.randint(0, len(quotes) - 1)]

def type_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        for _ in range(2000000): pass  # Delay loop
    print()

def interview_darth_vader():
    print("Welcome to the interview with Darth Vader!")
    print("You can ask him any question, and he will respond.")
    print("Type 'exit' to end the interview.\n")
    
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            type_slowly("Interview ended. May the Force be with you!")
            break
        if question.strip() == '':
            type_slowly("Please ask a question or type 'exit' to end the interview.\n")
            continue
        response = get_vader_response()
        type_slowly(f"Darth Vader: {response}\n")

if __name__ == "__main__":
    interview_darth_vader()
