import time
import random

def load_text():
    texts = [
        "Hello world this is a typing test",
        "Python is awesome for building projects",
        "Data analysis requires good typing speed",
        "Hyderabad is the best city for tech jobs",
        "Practice makes a man perfect in typing"
    ]
    return random.choice(texts)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    print("Press ENTER to begin...")
    input()

    target = load_text()
    print("\nType this:\n")
    print(f">>> {target}\n")

    start = time.time()
    typed = input("Your typing: ")
    end = time.time()

    time_taken = end - start
    minutes = time_taken / 60

    # WPM calculation
    wpm = round((len(typed) / 5) / minutes) if minutes > 0 else 0

    # Accuracy
    correct_chars = 0
    for i in range(min(len(target), len(typed))):
        if target[i] == typed[i]:
            correct_chars += 1

    accuracy = round((correct_chars / len(target)) * 100, 2)

    print("\n--- Result ---")
    print(f"Time: {round(time_taken, 2)} sec")
    print(f"WPM: {wpm}")
    print(f"Accuracy: {accuracy}%")

    if typed == target:
        print("Perfect! You typed correctly!")
    else:
        print(f"Original : {target}")
        print(f"You typed: {typed}")

while True:
    typing_test()
    print("\nPress ENTER to try again or type 'exit' to quit")
    choice = input().lower()
    if choice == 'exit':
        break