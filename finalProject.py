"""
Author: Trisha Atluri
Consulted:
Date: 2023-05-02
Purpose: Data analysis final project
"""

import csv

def disorderQuestion():
    """introduces analysis and asks the user for disorder to analyze"""
    disorder = int(input("Hi! Fancy seeing you here.\nJust thinking out loud for no particular reason with no particular end goal in mind, wouldn't it be nice if we could analyze associations between age, favorite music, and mental health?\nOH WAIT, we can!\nIn this analysis, we will calculate these associations for you.\nTo start, which disorder would you like to focus on? \n\nYour options are: \n1) Depression\n2) Anxiety\n3) Insomnia\n4) OCD\n\nAnswer here: "))
    return disorder

def musicQuestion():
    """asks the user for music genre to analyze"""
    genre = int(input("Out of the following music genres, which do you most prefer?\nYour options are:\n1) Rock\n2) Pop\n3) Metal\n4) Classical\n\nAnswer here: "))
    return genre

def musicUnder20(genre):
    """calculates the percentage of survey respondents under 20 years of age whose favorite genre is the same as the user's choice"""
    if genre == 1:
        genre = "Rock"
    elif genre == 2:
        genre = "Pop"
    elif genre == 3:
        genre = "Metal"
    elif genre == 4:
        genre = "Classical"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 4.55
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) < 20
                except ValueError:
                    pass
                if age:
                    total += 1
                if age and row["Fav genre"] == genre:
                    count += 1
            return round(count*100/total, 2)

def mentalUnder20(disorder):
    """calculates the percentage of survey respondents under 20 years of age who answered higher than 5 for the user's chosen disorder"""
    if disorder == 1:
        disorder = "Depression"
    elif disorder == 2:
        disorder = "Anxiety"
    elif disorder == 3:
        disorder = "Insomnia"
    elif disorder == 4:
        disorder = "OCD"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 32.78
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) < 20
                except ValueError:
                    pass
                if age:
                    total += 1
                try:
                    scale = int(row[disorder]) > 5
                except ValueError:
                    pass
                if age and scale:
                    count += 1
            return round(count*100/total, 2)

def music20to30(genre):
    """calculates the percentage of survey respondents who are 20-30 years old whose favorite genre is the same as the user's choice"""
    if genre == 1:
        genre = "Rock"
    elif genre == 2:
        genre = "Pop"
    elif genre == 3:
        genre = "Metal"
    elif genre == 4:
        genre = "Classical"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 10.34
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) > 19 and int(row["Age"]) < 31
                except ValueError:
                    pass
                if age:
                    total += 1
                if age and row["Fav genre"] == genre:
                    count += 1
            return round(count*100/total, 2)

def mental20to30(disorder):
    """calculates the percentage of survey respondents who are 20-30 years old who answered higher than 5 for the user's chosen disorder"""
    if disorder == 1:
        disorder = "Depression"
    elif disorder == 2:
        disorder = "Anxiety"
    elif disorder == 3:
        disorder = "Insomnia"
    elif disorder == 4:
        disorder = "OCD"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 2.69
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) > 19 and int(row["Age"]) < 31
                except ValueError:
                    pass
                if age:
                    total += 1
                try:
                    scale = int(row[disorder]) > 5
                except ValueError:
                    pass
                if age and scale:
                    count += 1
            return round(count*100/total, 2)

def musicOver30(genre):
    """calculates the percentage of survey respondents over 30 years of age whose favorite genre is the same as the user's choice"""
    if genre == 1:
        genre = "Rock"
    elif genre == 2:
        genre = "Pop"
    elif genre == 3:
        genre = "Metal"
    elif genre == 4:
        genre = "Classical"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 64.44
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) > 30
                except ValueError:
                    pass
                if age:
                    total += 1
                if age and row["Fav genre"] == genre:
                    count += 1
            return round(count*100/total, 2)

def mentalOver30(disorder):
    """calculates the percentage of survey respondents over 30 years of age who answered higher than 5 for the user's chosen disorder"""
    if disorder == 1:
        disorder = "Depression"
    elif disorder == 2:
        disorder = "Anxiety"
    elif disorder == 3:
        disorder = "Insomnia"
    elif disorder == 4:
        disorder = "OCD"
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            return 27.59
        else:
            total = 0
            count = 0
            for row in rows:
                try:
                    age = int(row["Age"]) > 30
                except ValueError:
                    pass
                if age:
                    total += 1
                try:
                    scale = int(row[disorder]) > 5
                except ValueError:
                    pass
                if age and scale:
                    count += 1
            return round(count*100/total, 2)

def preference():
    """calculates what genre the user is most likely to prefer based on their age and the survey data"""
    userAge = int(input("Just curious, how old are you?\nOr, if you're afraid that we'll sell this information to Big Pharma (even though I'm just a college freshman and not storing this data), give us a random age.\nAnswer here: "))
    if userAge < 20:
        a = musicUnder20(1)
        b = musicUnder20(2)
        c = musicUnder20(3)
        d = musicUnder20(4)
        highest = max(a, b, c, d)
        if highest == a:
            return ["rock", highest]
        elif highest == b:
            return ["pop", highest]
        elif highest == c:
            return ["metal", highest]
        elif highest == d:
            return ["classical", highest]
    elif userAge > 19 and userAge < 31:
        a = music20to30(1)
        b = music20to30(2)
        c = music20to30(3)
        d = music20to30(4)
        highest = max(a, b, c, d)
        if highest == a:
            return ["rock", highest]
        elif highest == b:
            return ["pop", highest]
        elif highest == c:
            return ["metal", highest]
        elif highest == d:
            return ["classical", highest]
    elif userAge > 30:
        a = musicOver30(1)
        b = musicOver30(2)
        c = musicOver30(3)
        d = musicOver30(4)
        highest = max(a, b, c, d)
        if highest == a:
            return ["rock", highest]
        elif highest == b:
            return ["pop", highest]
        elif highest == c:
            return ["metal", highest]
        elif highest == d:
            return ["classical", highest]

def summary(genres):
    """prints the average likert scale answer for each disorder for people whose favorite genre is rock, pop, metal, or classical."""
    disorders = ["Depression", "Anxiety", "Insomnia", "OCD"]
    if len(genres) == 0:
        return
    else:
        for disorder in disorders:
            with open("data.csv", "r") as data:
                reader = csv.DictReader(data)
                rows = [dict(row) for row in reader]
                if len(rows) == 0:
                    print("Never mind.")
                    return
                else:
                    total = 0
                    count = 0
                    for row in rows:
                        if row["Fav genre"] == genres[0]:
                            count += 1
                            try:
                                disorderScore = int(row[disorder])
                                total += disorderScore
                            except ValueError:
                                pass
                    print(f"{genres[0]}/{disorder} - {round(total/count, 1)}")
        print("")
    genres = genres[1:]
    return summary(genres)               
            
def main():
    """analyzes music genre and mental disorder survey data to compare
    associations across age groups."""
    disorder = disorderQuestion()
    print("")
    genre = musicQuestion()
    with open("data.csv", "r") as data:
        reader = csv.DictReader(data)
        rows = [dict(row) for row in reader]
        if len(rows) == 0:
            print("No data in chosen file. We'll print random numbers for the analysis.")
    print("\nBefore we get into the analysis, we'd like to provide you with some background on the survey used to gather this data.\n\nAmong other questions, survey respondents answered various questions about music, including one about their favorite genre.\nThey also ranked their experiences with the 4 mental disorders listed above on a scale of 0 to 10, where 0 corresponds with an answer of 'I do not experience this' and 10 corresponds with 'I experience this regularly, constantly/or to an extreme.'\n\nNow let's get into the analysis.")
    under20 = musicUnder20(genre)
    between2030 = music20to30(genre)
    over30 = musicOver30(genre)
    under20mental = mentalUnder20(disorder)
    between2030mental = mental20to30(disorder)
    over30mental = mentalOver30(disorder)
    print(f"\nHere are the age demographics for your chosen music genre:\n\n{under20}% of respondents under 20 years old have the same favorite music genre as you.\n{between2030}% of respondents who are 20 to 30 years old have the same favorite music genre as you.\n{over30}% of respondents over 30 years old have the same favorite music genre as you.")
    if disorder == 1:
        disorder = "Depression"
    elif disorder == 2:
        disorder = "Anxiety"
    elif disorder == 3:
        disorder = "Insomnia"
    elif disorder == 4:
        disorder = "OCD"
    print(f"\nHere are the age demographics for your chosen disorder:\n\n{under20mental}% of respondents under 20 years old scored themselves greater than 5 for {disorder}.\n{between2030mental}% of respondents who are 20 to 30 years old scored themselves greater than 5 for {disorder}.\n{over30mental}% of respondents over 30 years old scored themselves greater than 5 for {disorder}.")
    print("")
    prefer = preference()
    print(f"\nThank you for trusting us with that information (or not).\n\nBased on your age and the survey data, you are most likely to prefer {prefer[0]} music. {prefer[1]}% of people in your age range said {prefer[0]} was their favorite genre.") 
    print("\nFor our last trick, we will leave you with some general averages. In the list that follows, you will see the average scale answer for each disorder among people whose favorite music genre was rock, pop, metal, or classical.\n")
    summary(["Rock", "Pop", "Metal", "Classical"])
    print("That's all we have for you! Have a lovely day <3")

main()