import time
import random
from datetime import datetime, timedelta

class Task:
    def __init__(self, name, deadline, reward=10, xp=10):
        self.name = name
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d')
        self.completed = False
        self.reward = reward
        self.xp = xp

    def complete_task(self):
        if not self.completed:
            self.completed = True
            return self.reward, self.xp
        return 0, 0

class Pomodoro:
    @staticmethod
    def start_pomodoro(duration=25, break_time=5):
        time.sleep(duration * 60)
        Pomodoro.random_event()
        time.sleep(break_time * 60)
    
    @staticmethod
    def random_event():
        events = [
            "You found a rare book! +10 XP",
            "A sudden inspiration strikes! +5 credits",
            "You got distracted and lost some energy.",
            "A pet kept you company! +5 energy"
        ]
        print(random.choice(events))

class Player:
    def __init__(self, name):
        self.name = name
        self.credits = 0
        self.tasks = []
        self.house_level = 1
        self.garden = []
        self.pets = []
        self.inventory = {}
        self.energy = 100
        self.level = 1
        self.xp = 0

    def add_task(self, task_name, deadline, reward=10, xp=10):
        self.tasks.append(Task(task_name, deadline, reward, xp))

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name and not task.completed:
                reward, xp = task.complete_task()
                self.credits += reward
                self.energy = min(self.energy + 10, 100)
                self.gain_xp(xp)
                return

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 50:
            self.level += 1
            self.xp = 0
            print(f"Congratulations! {self.name} reached level {self.level}!")

    def buy_item(self, item, cost):
        if self.credits >= cost:
            self.credits -= cost
            self.inventory[item] = self.inventory.get(item, 0) + 1
            return True
        return False

    def buy_pet(self, pet_name):
        if self.buy_item(pet_name, 30):
            self.pets.append(pet_name)

    def buy_garden_item(self, item_name):
        if self.buy_item(item_name, 20):
            self.garden.append(item_name)

    def buy_drink(self, drink):
        drinks = {"Coffee": 10, "Energy Drink": 20, "Tea": 5}
        boosts = {"Coffee": 15, "Energy Drink": 30, "Tea": 10}
        if drink in drinks and self.buy_item(drink, drinks[drink]):
            self.energy = min(self.energy + boosts[drink], 100)

    def upgrade_house(self):
        if self.buy_item("House Upgrade", 50 * self.house_level):
            self.house_level += 1

    def sell_item(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            self.inventory[item] -= 1
            self.credits += 10
        elif item in self.garden:
            self.garden.remove(item)
            self.credits += 10
        elif item in self.pets:
            self.pets.remove(item)
            self.credits += 15

    def show_status(self):
        print(f"Player: {self.name}")
        print(f"Level: {self.level} | XP: {self.xp}")
        print(f"Credits: {self.credits}")
        print(f"Energy: {self.energy}")
        print(f"House Level: {self.house_level}")
        print(f"Garden: {', '.join(self.garden) if self.garden else 'Empty'}")
        print(f"Pets: {', '.join(self.pets) if self.pets else 'None'}")
        print(f"Inventory: {self.inventory}")
        for task in self.tasks:
            status = "✓" if task.completed else "✗"
            print(f"  [{status}] {task.name} (Due: {task.deadline.strftime('%Y-%m-%d')})")

    def rest(self):
        self.energy = min(self.energy + 20, 100)

    def work(self, hours):
        if self.energy >= hours * 10:
            self.credits += hours * 5
            self.energy -= hours * 10

player = Player("Danny")
player.add_task("Study Python", "2025-02-20", 15, 20)
player.complete_task("Study Python")
player.buy_pet("Cat")
player.buy_garden_item("Apple Tree")
player.upgrade_house()
player.buy_drink("Coffee")
player.work(3)
player.rest()
Pomodoro.start_pomodoro()
player.show_status()
