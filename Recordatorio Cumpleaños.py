  import datetime
import os

BIRTHDAYS_FILE = 'birthdays.txt'

def load_birthdays():
    birthdays = {}
    if os.path.exists(BIRTHDAYS_FILE):
        with open(BIRTHDAYS_FILE, 'r') as f:
            for line in f:
                name, date = line.strip().split(',')
                birthdays[name] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    return birthdays

def save_birthdays(birthdays):
    with open(BIRTHDAYS_FILE, 'w') as f:
        for name, date in birthdays.items():
            f.write(f'{name},{date}\n')

def add_birthday(birthdays):
    name = input("Person's name: ")
    date_str = input("Birthday date (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    birthdays[name] = date
    save_birthdays(birthdays)
    print(f"{name}'s birthday added for {date}.")

def remind_birthdays(birthdays):
    today = datetime.date.today()
    upcoming_days = 7
    for name, date in birthdays.items():
        next_birthday = date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = date.replace(year=today.year + 1)
        
        days_until = (next_birthday - today).days
        if 0 <= days_until <= upcoming_days:
            print(f"{name}'s birthday is in {days_until} days ({next_birthday}).")

def menu():
    birthdays = load_birthdays()
    while True:
        print("\n1. Add birthday")
        print("2. View upcoming birthdays")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == '1':
            add_birthday(birthdays)
        elif option == '2':
            remind_birthdays(birthdays)
        elif option == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu()
