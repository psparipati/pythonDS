"""
Calculations and datasets were derived from https://www.kaggle.com/competitions/titanic/data
"""

import pandas as pd


titanic = pd.read_csv('titanic_data.csv')


def pure_numbers():
    count_of_pure_numbers = titanic['Ticket'].str.isnumeric().sum()
    print(f"\nHow many of the tickets are pure numbers?\n"
          f"From the data, we calculated that there are {count_of_pure_numbers} tickets that are pure numbers.")


def survivors_vs_fatalities():
    print("\nHow many people survived the Titanic, and how many people died?")
    print(f"From the data, we calculated that {titanic['Survived'].sum()} people"
          f" survived the Titanic and {len(titanic) - titanic['Survived'].sum()} people died from the Titanic.")


if __name__ == '__main__':
    survivors_vs_fatalities()
    pure_numbers()
