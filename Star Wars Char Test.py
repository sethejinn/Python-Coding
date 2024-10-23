def main():
    print("Welcome to the Star Wars Character Quiz!")
    print("Answer the following questions to find out which Star Wars character you are.")

    character_scores = {
        "Luke Skywalker": 0,
        "Princess Leia": 0,
        "Han Solo": 0,
        "Darth Vader": 0,
        "Yoda": 0,
        "Obi-Wan Kenobi": 0,
        "Chewbacca": 0,
        "R2-D2": 0,
        "C-3PO": 0,
        "Boba Fett": 0,
        "Emperor Palpatine": 0
    }

    print("\nQuestion 1: What is your preferred weapon?")
    print("a) Lightsaber")
    print("b) Blaster")
    answer = input("Your choice (a/b): ").lower()
    if answer == "a":
        character_scores["Luke Skywalker"] += 1
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
    elif answer == "b":
        character_scores["Princess Leia"] += 1
        character_scores["Han Solo"] += 1
        character_scores["Darth Vader"] += 1

    print("\nQuestion 2: What motivates you?")
    print("a) Seeking adventure")
    print("b) Fighting for justice")
    print("c) Gaining power")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Han Solo"] += 1
        character_scores["Chewbacca"] += 1
        character_scores["R2-D2"] += 1
    elif answer == "b":
        character_scores["Luke Skywalker"] += 1
        character_scores["Princess Leia"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
        character_scores["C-3PO"] += 1
    elif answer == "c":
        character_scores["Darth Vader"] += 1
        character_scores["Emperor Palpatine"] += 1
        character_scores["Boba Fett"] += 1

    print("\nQuestion 3: What is your approach to problem-solving?")
    print("a) Use the Force")
    print("b) Rely on technology")
    print("c) Trust your instincts")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Luke Skywalker"] += 1
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
    elif answer == "b":
        character_scores["R2-D2"] += 1
        character_scores["C-3PO"] += 1
    elif answer == "c":
        character_scores["Han Solo"] += 1
        character_scores["Chewbacca"] += 1
        character_scores["Darth Vader"] += 1
        character_scores["Boba Fett"] += 1

    print("\nQuestion 4: What is your ideal role in a team?")
    print("a) Leader")
    print("b) Strategist")
    print("c) Loyal companion")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Luke Skywalker"] += 1
        character_scores["Princess Leia"] += 1
        character_scores["Darth Vader"] += 1
    elif answer == "b":
        character_scores["Obi-Wan Kenobi"] += 1
        character_scores["Yoda"] += 1
        character_scores["Emperor Palpatine"] += 1
    elif answer == "c":
        character_scores["Han Solo"] += 1
        character_scores["Chewbacca"] += 1
        character_scores["R2-D2"] += 1
        character_scores["C-3PO"] += 1

    print("\nQuestion 5: How do you handle stress?")
    print("a) Meditation or calm reflection")
    print("b) Taking action and solving the problem")
    print("c) Delegating tasks to others")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
    elif answer == "b":
        character_scores["Luke Skywalker"] += 1
        character_scores["Han Solo"] += 1
        character_scores["Princess Leia"] += 1
        character_scores["Boba Fett"] += 1
    elif answer == "c":
        character_scores["Darth Vader"] += 1
        character_scores["Emperor Palpatine"] += 1
        character_scores["C-3PO"] += 1

    print("\nQuestion 6: What kind of environment do you thrive in?")
    print("a) A calm, peaceful setting")
    print("b) An active, bustling city")
    print("c) A place with constant challenges")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
        character_scores["Luke Skywalker"] += 1
    elif answer == "b":
        character_scores["Han Solo"] += 1
        character_scores["Princess Leia"] += 1
        character_scores["R2-D2"] += 1
        character_scores["C-3PO"] += 1
    elif answer == "c":
        character_scores["Darth Vader"] += 1
        character_scores["Emperor Palpatine"] += 1
        character_scores["Boba Fett"] += 1

    print("\nQuestion 7: How do you prefer to travel?")
    print("a) By starship")
    print("b) On foot")
    print("c) By speeder")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Han Solo"] += 1
        character_scores["Chewbacca"] += 1
        character_scores["Luke Skywalker"] += 1
    elif answer == "b":
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
        character_scores["R2-D2"] += 1
    elif answer == "c":
        character_scores["Princess Leia"] += 1
        character_scores["Darth Vader"] += 1
        character_scores["Boba Fett"] += 1

    print("\nQuestion 8: What is your greatest strength?")
    print("a) Wisdom")
    print("b) Bravery")
    print("c) Intelligence")
    answer = input("Your choice (a/b/c): ").lower()
    if answer == "a":
        character_scores["Yoda"] += 1
        character_scores["Obi-Wan Kenobi"] += 1
    elif answer == "b":
        character_scores["Luke Skywalker"] += 1
        character_scores["Han Solo"] += 1
        character_scores["Princess Leia"] += 1
        character_scores["Chewbacca"] += 1
    elif answer == "c":
        character_scores["R2-D2"] += 1
        character_scores["C-3PO"] += 1
        character_scores["Emperor Palpatine"] += 1

    # Highest score
    max_score = max(character_scores.values())
    top_characters = [char for char, score in character_scores.items() if score == max_score]

    print("\nYou are most like:")
    for character in top_characters:
        print("-", character)

if __name__ == "__main__":
    main()

    main()
