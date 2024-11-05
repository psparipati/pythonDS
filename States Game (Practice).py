import random
import pandas as pd

# Assume "states_and_capitals.csv" is a CSV sheet with states in one column and capital cities in another column.
states_library = pd.read_csv("states_and_capitals.csv").set_index("State")["Capital City"].to_dict()

i = 0
correct_answers = 0
while i < 5:
    choices = list(states_library.keys())
    state = random.choice(choices)
    query = input(f"What is the state capital of {state}?\n\n")
    if query == states_library[state]:
        correct_answers = correct_answers + 1
    i = i + 1
    choices.remove(state)
print(f"Final Score: {correct_answers} out of 5")
