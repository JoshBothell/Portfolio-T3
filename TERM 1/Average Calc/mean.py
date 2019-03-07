#JoshBothell
#9/17/18

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
            print(mean)
        #cancels loop
        elif com == "end":
            x = x + 1
        else:
            print("Sorry! I didn't understand that command")

#function to find mean of predetermined list from the program.
avg_score()

def avg_list(lst):
    return sum(lst) / len(lst)

list1 = [100, 125, 175, 200]

#catching return
mlist1 = avg_list(list1)
print(mlist1)
    
  
