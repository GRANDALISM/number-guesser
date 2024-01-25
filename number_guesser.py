import random

players = input("How many Players? ")

while not players.isdigit() or int(players) <= 0:
    print("Please enter a valid number of players.")
    players = input("How many Players? ")

top_of_range = input(f"What are your odds? It should be at least {int(players) + 1} The higher the number the more suspense: ")

while not top_of_range.isdigit() or int(top_of_range) <= int(players):
    print(f"Please enter a valid odds value, at least {int(players) + 1}.")
    top_of_range = input("What are your odds? ")

top_of_range = int(top_of_range)

random_number = random.randint(1, top_of_range)

while True:
    user_guess = input("Guessing time: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if not 1 <= user_guess <= top_of_range:
            print(f"Please guess a number between 1 and {top_of_range} ")
            continue
    else:
        print("That's not how odds work and you know it. Please select a number ")
        continue

    if user_guess == random_number:
        print("We have a match, You've been nominated")
        break
    else:
        print("Lucky day, you missed")
        top_of_range -= 1
        print(f"Odds reduced to {top_of_range}")

        if top_of_range == 0:
            print("How did you get this far, I smell a cheat")
            break

        random_number = random.randint(1, top_of_range)
        print(f"CONGRATULATIONS, A new random number is generated between 1 and {top_of_range}. Make your new guess")