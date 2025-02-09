import time
import random

class Samurai:
    def __init__(self, name, samurai_class):
        self.name = name
        self.level = 1
        self.exp = 0
        self.health = 100
        self.energy = 100
        self.coins = 50
        self.inventory = []
        self.missions_completed = 0
        self.reputation = 0
        self.clan = None
        self.weapon = "Wooden Sword"
        self.armor = "Cloth Armor"
        self.samurai_class = samurai_class
        self.assign_class_attributes()

    def assign_class_attributes(self):
        classes = {
            "Ronin": {"strength": 7, "agility": 5, "defense": 3},
            "Bushido": {"strength": 5, "agility": 7, "defense": 4},
            "Shogun": {"strength": 6, "agility": 4, "defense": 6}
        }
        attrs = classes.get(self.samurai_class, classes["Ronin"])
        self.strength = attrs["strength"]
        self.agility = attrs["agility"]
        self.defense = attrs["defense"]

    def train(self):
        if self.energy >= 10:
            self.energy -= 10
            self.strength += random.randint(1, 3)
            self.agility += random.randint(1, 3)
            self.defense += random.randint(1, 2)
            print(f"{self.name} has trained! Strength: {self.strength}, Agility: {self.agility}, Defense: {self.defense}")
        else:
            print("Not enough energy to train!")

    def rest(self):
        print(f"{self.name} is resting...")
        time.sleep(2)
        self.energy = min(100, self.energy + 30)
        self.health = min(100, self.health + 20)
        print(f"Energy restored to {self.energy}, Health restored to {self.health}")

    def fight(self, enemy):
        if self.energy < 20:
            print("Not enough energy to fight!")
            return
        
        self.energy -= 20
        print(f"{self.name} engages in battle with {enemy['name']}!")
        player_attack = self.strength + random.randint(0, 5) - enemy['defense']
        enemy_attack = enemy['strength'] + random.randint(0, 5) - self.defense

        if player_attack > enemy_attack:
            print(f"{self.name} wins the fight!")
            self.exp += 30
            self.coins += 20
            self.missions_completed += 1
            self.reputation += 5
        else:
            print(f"{self.name} loses and takes damage!")
            self.health -= 15

        if self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.strength += 3
        self.agility += 3
        self.defense += 2
        self.health = 100
        self.energy = 100
        print(f"{self.name} has leveled up to Level {self.level}!")

    def shop(self):
        items = {"Iron Sword": 30, "Steel Katana": 50, "Samurai Armor": 70, "Health Potion": 15}
        print("Welcome to the shop! Items available:")
        for item, price in items.items():
            print(f"{item}: {price} coins")
        choice = input("What would you like to buy? ")
        if choice in items and self.coins >= items[choice]:
            self.coins -= items[choice]
            if "Potion" in choice:
                self.inventory.append(choice)
            else:
                self.weapon = choice
            print(f"{self.name} bought {choice}!")
        else:
            print("Not enough coins or invalid choice!")
    
    def use_item(self, item):
        if item in self.inventory:
            if item == "Health Potion":
                self.health = min(100, self.health + 30)
                self.inventory.remove(item)
                print(f"{self.name} used a {item} and restored health to {self.health}")
        else:
            print("Item not available in inventory!")

    def mission(self):
        print("Embarking on a mission...")
        time.sleep(2)
        success = random.choice([True, False])
        if success:
            reward = random.randint(20, 50)
            self.coins += reward
            self.exp += 40
            self.missions_completed += 1
            self.reputation += 10
            print(f"Mission successful! Earned {reward} coins and 40 XP. Reputation increased!")
        else:
            print("Mission failed. Try again later!")
        if self.exp >= 100:
            self.level_up()

print("Welcome to the Samurai RPG!")
name = input("Enter your samurai's name: ")
print("Choose your class: Ronin, Bushido, Shogun")
samurai_class = input("Enter your class: ")
player = Samurai(name, samurai_class)

enemies = [
    {"name": "Bandit", "strength": 5, "defense": 2},
    {"name": "Ronin", "strength": 7, "defense": 3},
    {"name": "Warlord", "strength": 10, "defense": 5}
]

while True:
    print("\nActions: Train, Rest, Fight, Shop, Use Item, Mission, Clan, Exit")
    action = input("What would you like to do? ").lower()
    if action == "train":
        player.train()
    elif action == "rest":
        player.rest()
    elif action == "fight":
        player.fight(random.choice(enemies))
    elif action == "shop":
        player.shop()
    elif action == "use item":
        item = input("Enter item name: ")
        player.use_item(item)
    elif action == "mission":
        player.mission()
    elif action == "clan":
        print("Clans will be implemented soon!")
    elif action == "exit":
        print("Goodbye, warrior!")
        break
    else:
        print("Invalid action!")
