#JoshBothell
#10/5
#Average Calculator


#user creates list to find mean from
def avg_score():
#creating a list for the test scores
    scores = []
#looping input question
    x = 1
    while x < 2:
        #asking for a command to activate a number of options
        com = input("Type a command, either 'ADD' to add a score or 'MEAN' to get the current average. \n If you are finished type 'END' to continue.   ")
        com = com.lower()
        #appends a float to the list
        if com == "add":
            nscore = float(input("Enter the score to be added: "))
            scores.append(nscore)
        #dividing the sum by the length
        elif com == "mean":
            mean = sum(scores) / len(scores)
            return mean
            x = x+1

#function to find mean of predetermined list from the program.
mean = avg_score()
if mean >= 90:
    grade = "A"
else:
    if mean >= 80:
        grade = "B"
    else:
        if mean >= 70:
            grade = "C"
        else:
            if mean >= 60:
                grade = "D"
            else:
                if mean >= 50:
                    grade = "F"
                else:
                    grade = "F"
print("Your grade is", grade, "with an average of ", mean)
