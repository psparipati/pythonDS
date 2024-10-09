from import_before_assignment import random

def computer_colors():
    computer = []
    possible_colors = ["Red", "Yellow", "Green", "Blue", "Black", "White"]
    i = 0
    while i != 4:
        choice = random.choice(possible_colors)
        computer.append(choice)
        possible_colors.remove(choice)
        i += 1
    del i
    return computer


def cows_and_bulls(computer, player):
    cows = 0
    bulls = 0
    if len(computer) != len(player):
        raise ValueError("You didn't do it correctly, it's supposed to be 4 colors.")
    else:
        i = 0
        while i != 4:
            if player[i] in computer:
                if player[i] == computer[i]:
                    bulls += 1
                else:
                    cows += 1
            i += 1
    return [bulls, cows]


while True:
    print("\nI am creating a sequence for you.\nGenerating colors...\n")
    computer = computer_colors()
    print("Red\nYellow\nGreen\nBlue\nBlack\nWhite\n")
    print("Select 4 colors from the following, typing each color as it appears followed by a space.\nIf you enter duplicates, I'll know.")
    guess = 0
    has_won = False
    while guess != 8:
        colors = input("Enter your colors here:\t")
        colors = colors.split(" ")
        if len(colors) != len(set(colors)):
            print("I told you I'd find out.")
            continue
        l = cows_and_bulls(computer, colors)
        if l[0] == 4:
            print("\nYay, you did it!")
            has_won = True
            guess = 8
        else:
            print(f"\nBulls: {l[0]} Cows: {l[1]}\n")
            print(f"You have {7 - guess} guesses left.\n")
            guess += 1
    if has_won == False:
        print(f"You lost. I picked this {computer}")
    d = int(input("Enter 1 to continue playing, enter 0 to end the game. "))
    if d == 0:
        break
    elif d == 1:
        continue
