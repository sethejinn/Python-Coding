def choose_random(lst):

    index = int((len(lst) * (hash(str(lst)) % 100) / 100)) % len(lst)
    return lst[index]

def delay(seconds):

    target_time = seconds * 10**6  # Convert seconds to microseconds
    start_time = 0
    while start_time < target_time:
        start_time += 1

def jedi_vs_sith_battle():

    jedis = [
        "Luke Skywalker", "Obi-Wan Kenobi", "Yoda", "Anakin Skywalker", 
        "Qui-Gon Jinn", "Ahsoka Tano", "Revan", "Meetra Surik", "Mace Windu", 
        "Ki-Adi-Mundi", "Plo Koon", "Shaak Ti", "Bastila Shan", "Jolee Bindo",
        "Kanan Jarrus", "Ezra Bridger", "Cal Kestis", "Depa Billaba", "Aayla Secura", 
        "Luminara Unduli", "Kit Fisto", "Cere Junda", "Eeth Koth", "Jocasta Nu",
        "Satele Shan", "Stass Allie", "Adi Gallia", "Vrook Lamar", "Zayne Carrick",
        "Quinlan Vos", "Coleman Trebor", "Nomi Sunrider", "Kyp Durron", "Kyle Katarn"
    ]

    siths = [
        "Darth Vader", "Darth Maul", "Emperor Palpatine", "Count Dooku", 
        "Darth Bane", "Darth Nihilus", "Darth Malak", "Darth Revan", "Darth Sion", 
        "Darth Malgus", "Starkiller", "Asajj Ventress", "Savage Opress", "Darth Traya",
        "The Grand Inquisitor", "Darth Plagueis", "Darth Zannah", "Darth Krayt", 
        "Barriss Offee", "Second Sister (Trilla Suduri)", "Fifth Brother", "Eighth Brother",
        "Darth Talon", "Darth Caedus", "Darth Marr", "Darth Vitiate", "Darth Tenebrous",
        "Darth Ruin", "Darth Wyyrlok", "Darth Nihl", "Mother Talzin", "Kylo Ren"
    ]

    print("The battle begins!")
    delay(2)  # Wait for 2 seconds

    jedi = choose_random(jedis)
    sith = choose_random(siths)

    print(f"{jedi} faces {sith}")
    delay(2)  # Wait for 2 seconds

    winner = choose_random([jedi, sith])
    if winner in jedis:
        result = "The Jedi has won!"
    else:
        result = "The Sith has won!"

    print(result)
    delay(2)

def main():
    while True:
        jedi_vs_sith_battle()
        repeat = input("Do you want to simulate another battle? (y/n): ")
        if repeat.lower() != 'y':
            break
        delay(2)  # Wait for 2 seconds before the next simulation

if __name__ == "__main__":
    main()
