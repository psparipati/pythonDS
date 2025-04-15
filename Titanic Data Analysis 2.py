import pandas as pd

# Download from https://github.com/datasciencedojo/datasets/blob/master/titanic.csv as titanic.csv
titanic = pd.read_csv("Python/PythonDS/Assignment 6/titanic.csv")


def question_1():
    return ["Retrieve the first 10 rows of the dataset.",
            titanic.head(10)]


def question_2():
    return ["Display the columns Name, Age, and Survived for passengers with a Pclass value of 1.",
            titanic[titanic['Pclass'] == 1][['Name', 'Age', 'Survived']]]


def question_3():
    return ["Find and display all rows where passengers are aged above 60.",
            titanic[titanic['Age'] > 60]]


def question_4():
    return ["Locate the row(s) for the passenger(s) with the maximum fare (Fare).",
            titanic[titanic['Fare'] == titanic['Fare'].max()]]


def question_5():
    return ["Retrieve the Name and Ticket of passengers who embarked from port C (Cherbourg).",
            titanic[titanic['Embarked'] == 'C'][['Name', 'Ticket']]]


def question_6():
    return ["Display the Name, Age, and Cabin for passengers who do not have a cabin assigned (where Cabin is NaN).",
            titanic[titanic['Cabin'].isna()][['Name', 'Age', 'Cabin']]]


def question_7():
    return ["Retrieve the last 5 rows of the dataset.",
            titanic.tail()]


def question_8():
    return ["Locate the rows where the Survived value is 0 and display the PassengerId, Name, and Sex.",
            titanic[titanic['Survived'] == 0][['PassengerId', 'Name', 'Sex']]]


def question_9():
    return ["Extract all unique values of the Embarked column.",
            titanic['Embarked'].unique()]


def question_10():
    return ["Select the rows of passengers with a Fare greater than 50 and sort them in descending order by Fare.",
            titanic[titanic['Fare'] > 50].sort_values(by='Fare', ascending=False)]


def all_questions(n):
    if n == 1:
        return question_1()
    elif n == 2:
        return question_2()
    elif n == 3:
        return question_3()
    elif n == 4:
        return question_4()
    elif n == 5:
        return question_5()
    elif n == 6:
        return question_6()
    elif n == 7:
        return question_7()
    elif n == 8:
        return question_8()
    elif n == 9:
        return question_9()
    elif n == 10:
        return question_10()
    else:
        pass


def get_answer():
    with open('Python/PythonDS/Assignment 6/assignment6_titanic_questions.txt', 'w') as file:
        file.write("####Titanic Dataset Questions and Answers####\n\n")
        i = 1
        while i != 11:
            x = all_questions(i)
            file.write(f"{i}. {x[0]}\n{x[1]}\n\n")
            i += 1


if __name__ == '__main__':
    get_answer()
    pass
