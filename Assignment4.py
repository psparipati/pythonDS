def add_to_dict_new(add_to):
    # The name will help us add this to the whole library.
    name = input("Enter the person's name (you will be writing their preferences): ")
    # Defining every other variable relevant to this operation.
    array = {}
    total_points = 100
    # Go through every color and ask the user.
    for color in all_colors:
        # Handling cases where everything has already been allocated, and there are still colors left.
        if total_points == 0:
            array[color] = 0
            continue
        # Error handling to handle empty lines or non-integers.
        try:
            points = int(input(
                f"\nEnter the amount of points you want to give to {color}."
                f"\nKeep in mind, you only have {total_points} left to assign.\n\n"))
        except ValueError:
            points = 0
        # Entering more than required causes you to spend the remaining points, and you will be redirected to the start.
        if points > total_points:
            print("That's way too much. Program has been stopped.")
            array[color] = total_points
            total_points = 0
            continue
        # Perform necessary calculations.
        array[color] = points
        total_points -= points
    # Add the dictionary and name to the whole thing.
    add_to[name] = array


def add_to_dict_prerecorded(dc, add_to):
    # Parse the key so that we get the name.
    name = str(dc.keys())
    name = name.removeprefix("dict_keys(['")
    name = name.removesuffix("'])")
    # We add it to the dictionary, simple as that.
    add_to[name] = dc[name]


def favorite_color(dc):
    # Extract the names of everyone.
    people = dc.keys()
    # Initialize all the other variables.
    preferences = []
    totals = {}
    # Setting the theoretical scoreboard.
    for color in all_colors:
        totals[color] = 0
    # Adding every person's response to the preferences list.
    for person in people:
        preferences.append(dc[person])
    # Updating the scoreboard with each packet.
    for packet in preferences:
        for color in all_colors:
            totals[color] += packet[color]
    # Giving the final result.
    print(f"\nThe highest rated color among all subjects is {max(totals, key=totals.get)}"
          f" with {totals[max(totals, key=totals.get)]} points.")


def machine():
    # Run the method that creates the variables.
    initialize()
    # Create an infinite(?) caller machine that will ask
    while True:
        # User-friendly implementation so that my friends and family understood what they needed to do.
        print("\nYou have six options for what you want to do.\n\n1. View All Data Points\n2. Add 1 Data Point"
              "\n3. Add Multiple Data Points\n4. Delete All Data Points\n5. Complete Data Analysis\n6. Exit Program")
        # If you don't enter what you want to do correctly, I'll send you back.
        try:
            i = int(input("\nEnter the number that corresponds to what you want to do: "))
        except ValueError:
            continue
        # Print the data points.
        if i == 1:
            print("\n", all_preferences_and_people)
        # Add one data point.
        elif i == 2:
            add_to_dict_new(add_to=all_preferences_and_people)
        # Add multiple data points.
        elif i == 3:
            count = int(input("How many people? "))
            while count != 0:
                add_to_dict_new(add_to=all_preferences_and_people)
                count -= 1
        # Delete all data points.
        elif i == 4:
            all_preferences_and_people.clear()
        # Complete Data Analysis
        elif i == 5:
            favorite_color(dc=all_preferences_and_people)
        # End the whole program.
        elif i == 6:
            break
        # I can't handle every integer, so I use this final statement to convince you to do the right input.
        else:
            continue


def initialize():
    # Introduction text will play once for you to understand.
    print("\nThis is a color survey program. \nThis program allows you to enter your preferences for different colors"
          ", with the ability to give different amounts of points to each. This doesn't have to stay to a single color."
          "\nHowever, if you have no feelings for a certain color, you can type 0 and you won't suffer any consequence."
          "\nFor example, I could designate 4 colors (Orange, Yellow, Blue, Green), and leave the rest as 0."
          "\nIt would look something like ...\n")
    # Demonstrating a possible dictionary that could be developed.
    print("Color     	 |  Score\n--------------------")
    practice_dict = {'Red': 0, 'Blue': 25, 'Yellow': 25, 'Green': 25, 'Pink': 0, 'Purple': 0, 'White': 0,
                                 'Magenta': 0, 'Orange': 25, 'Cyan': 0}
    for x in practice_dict:
        print(f"{x:<10}\t | \t{practice_dict[x]:<5}")
    # Creating all the variables that are needed for these instance, including recorded data.
    global all_preferences_and_people
    all_preferences_and_people = {}
    # Some of my friends put it all on Black (or Blue or Green).
    list_of_surveyed_people = [{'Prabhav': {'Red': 0, 'Blue': 25, 'Yellow': 25, 'Green': 25, 'Pink': 0, 'Purple': 0,
                                            'White': 0, 'Magenta': 0, 'Orange': 25, 'Cyan': 0}},
                               {'Samar': {'Red': 65, 'Blue': 5, 'Yellow': 5, 'Green': 5, 'Pink': 5,
                                          'Purple': 5, 'White': 0, 'Magenta': 5, 'Orange': 1, 'Cyan': 4}},
                               {'Om': {'Red': 40, 'Blue': 30, 'Yellow': 0, 'Green': 30, 'Pink': 0,
                                       'Purple': 0, 'White': 0, 'Magenta': 0, 'Orange': 0, 'Cyan': 0}},
                               {'Elliot': {'Red': 0, 'Blue': 0, 'Yellow': 0, 'Green': 100, 'Pink': 0,
                                           'Purple': 0, 'White': 0, 'Magenta': 0, 'Orange': 0, 'Cyan': 0}},
                               {'Alek': {'Red': 0, 'Blue': 100, 'Yellow': 0, 'Green': 0, 'Pink': 0,
                                         'Purple': 0, 'White': 0, 'Magenta': 0, 'Orange': 0, 'Cyan': 0}},
                               {'Nikhil': {'Red': 0, 'Blue': 100, 'Yellow': 0, 'Green': 0, 'Pink': 0,
                                           'Purple': 0, 'White': 0, 'Magenta': 0, 'Orange': 0, 'Cyan': 0}}]
    # Rapidly adding my survey responses using technology.
    for person in list_of_surveyed_people:
        add_to_dict_prerecorded(person, all_preferences_and_people)
    # Every color that is referenced so that no part of the code is confused.
    global all_colors
    all_colors = ['Red', 'Blue', 'Yellow', 'Green', 'Pink', 'Purple', 'White', 'Magenta', 'Orange', 'Cyan']


if __name__ == '__main__':
    # Defining the whole function of this program as one function makes it more user-friendly.
    # If anyone wants to see the whole function, they can just go further inside my code, where I make this like a caller machine and give it unique functionalities based on that idea.
    machine()
