import pandas as pd
titanic = pd.read_csv("Python/PythonDS/Assignment 7/titanic.csv")

# Task 1: Perform GroupBy Analysis in Excel
# This part is done externally.

# Task 2: Perform GroupBy Analysis Using Pandas
with open("Python/PythonDS/Assignment 7/Task2.txt", "w") as f:
    pclass = titanic.groupby('Pclass')
    f.write(f"Compute the count of survivors per each class.\n{pclass['Survived'].sum()}\n\n")
    f.write(f"Compute the average fare per passenger class.\n{pclass['Fare'].mean()}\n\n")
    f.write(f"Compute the average age per passenger class.\n{pclass['Age'].mean()}\n\n")

# Task 3: Perform Pivot Table Analysis Using Pandas
with open("Python/PythonDS/Assignment 7/Task3.txt") as f:
    p1 = titanic.pivot_table(index='Pclass', values='Survived', aggfunc='sum')
    p2 = titanic.pivot_table(index='Pclass', values='Fare', aggfunc='mean')
    p3 = titanic.pivot_table(index='Pclass', values='Age', aggfunc='mean')
    f.write(f"Compute the count of survivors per each class.\n{p1}\n\n")
    f.write(f"Compute the average fare per passenger class.\n{p2}\n\n")
    f.write(f"Compute the average age per passenger class.\n{p3}\n\n")
