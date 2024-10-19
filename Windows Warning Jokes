import tkinter as tk
from tkinter import messagebox
import random
import time
from tkinter.simpledialog import askinteger, askstring

# List of jokes
jokes = [
    "Your computer is taking a coffee break!",
    "Are you sure you know what you're doing?",
    "Warning: Your brain is running low on memory.",
    "Error 404: Common sense not found!",
    "Congratulations! You've won... absolutely nothing!",
    "System update: Your patience is now outdated.",
    "Your CPU is on strike. Pay it more cookies.",
    "Oops... looks like you just broke the internet!",
    "Please stop working. You're making the computer tired.",
    "Did you try turning off your brain and on again?",
    "Fun fact: The spacebar is not a real space.",
    "Windows has decided to take a nap. Good luck!",
    "Reminder: You are not a robot... or are you?",
    "Don't panic, but something definitely went wrong!",
    "Warning: Your to-do list is growing out of control."
]

# Function to show the joke in a popup window
def show_joke(joke_type="info", joke_text="", joke_title=""):
    if joke_type == "info":
        messagebox.showinfo(joke_title, joke_text)
    elif joke_type == "warning":
        messagebox.showwarning(joke_title, joke_text)
    elif joke_type == "error":
        messagebox.showerror(joke_title, joke_text)

# Function to handle the main joke display
def start_jokes():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Ask how many jokes the user wants to see
    joke_count = askinteger("Number of Jokes", "How many jokes do you want?", minvalue=1, maxvalue=20)
    if joke_count is None:  # If user cancels
        return
    
    # Ask how often the jokes should repeat
    repeat_count = askinteger("Repeat Jokes", "How many times should each joke repeat?", minvalue=1, maxvalue=5)
    if repeat_count is None:
        return
    
    # Ask for the interval between the popups
    interval = askinteger("Interval", "How many seconds between each joke?", minvalue=1, maxvalue=60)
    if interval is None:
        return
    
    # Ask for the joke type (info, warning, error)
    joke_type = askstring("Type of Joke", "Type 'info', 'warning', or 'error'.")
    if joke_type not in ["info", "warning", "error"]:
        joke_type = "info"  # Default value
    
    # Ask for a custom title for the popup window
    joke_title = askstring("Joke Title", "Enter a custom title for the popup (or leave blank).")
    if joke_title is None or joke_title.strip() == "":
        joke_title = "Joke Time"  # Default title

    # Show the jokes according to user settings
    for _ in range(joke_count):
        joke = random.choice(jokes)  # Select a random joke
        for _ in range(repeat_count):  # Repeat the joke as requested
            show_joke(joke_type, joke, joke_title)
            time.sleep(interval)  # Wait for the specified interval before the next joke

# Main menu function
def main_menu():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    while True:
        # Ask if the user wants to start the jokes
        option = messagebox.askquestion("Joke Menu", "Do you want to start the jokes?", icon='question')
        
        if option == 'yes':
            start_jokes()
        else:
            messagebox.showinfo("Exit", "Goodbye! But remember, the jokes never really stop...")
            break

if __name__ == "__main__":
    main_menu()
