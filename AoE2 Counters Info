units_info = {
    1: ("Militia-Line", "Skirmishers, Spearman-Line, Eagle Warriors, Scouts", "Archers, Knights, Cavalry Archers, Hand Cannoneers"),
    2: ("Archer-Line", "Militia-Line, Spearman-Line, Knights (when in mass), Monks", "Eagle Warriors, Skirmishers, Siege"),
    3: ("Knight-Line", "Militia-Line, Archer-Line (in equal numbers), Scout-Line, Siege, Eagle Warriors", "Monks, Archer-Line (when at number disadvantage), Spearman-Line, Cavalry Archers (when at number disadvantage), Camels"),
    4: ("Spearman-Line", "Scout-Line, Knight-Line, Camels, Siege, Battle Elephants", "Archer-Line, Cavalry Archers, Hand Cannoneers, Skirmishers"),
    5: ("Skirmishers", "Spearman-Line, Archer-Line, Monks", "Knight-Line, Militia-Line, Camels, Scout-Line, Siege, Eagle Warriors"),
    6: ("Scout-Line", "Skirmishers, Monks, Siege, Archer-Line (in the early game in equal numbers)", "Knight-Line, Camels, Cavalry Archers, Archer-Line (in the late game unless at a greater amount), Militia-Line, Eagle Warriors"),
    7: ("Monks", "Knight-Line, Battle Elephant, Camels, Siege (when redemption is available)", "Scout-Line, Eagle Warriors, Archer-Line, Skirmishers, Spearman-Line"),
    8: ("Eagle Warriors", "Archer-Line, Skirmishers, Scout-Line (only when Eagle Warrior technology is researched), Monks, Siege", "Knight-Line, Militia-Line, Hand Cannoneers"),
    9: ("Camels", "Scout-Line, Knight-Line, Siege, Skirmishers", "Monks, Spearman-Line, Archer-Line"),
    10: ("Cavalry Archers", "Spearman-Line (with hit and run technique), Militia-Line, Knights (when in a greater mass), Camels (with hit-and-run technique)", "Skirmishers, Siege, Monks, Spearman-Line (without hit-and-run technique), Camels (without hit-and-run technique)"),
    11: ("Hand Cannoneers", "Infantry Units (Militia-Line, Eagle Warriors, Spearman-Line), Knights (when in mass), Scout-Line (in equal numbers), Camels", "Siege, Skirmishers, Knight-Line, Scout-Line, Archer-Line"),
    12: ("Battle Elephants", "Strong against all units provided it can reach that unit", "Spearman-Line, Monks, Archers (with Hit-and-Run technique), Cavalry Archers (with hit-and-run technique)")
}

def main():
    print("Welcome to the Sethejinn Age of Empires 2 Counter Identifier")
    print("Choose a unit by entering the corresponding number:")
    for key, value in units_info.items():
        print(f"{key}. {value[0]}")
    
    while True:
        try:
            choice = int(input("Enter the number of the unit: "))
            if choice in units_info:
                unit, good_against, weak_against = units_info[choice]
                print(f"\nUnit: {unit}")
                print(f"Good Against: {good_against}")
                print(f"Weak Against: {weak_against}\n")
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
