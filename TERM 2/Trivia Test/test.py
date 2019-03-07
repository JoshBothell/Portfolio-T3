#Josh Bothell
#1/19
#Trivia Challenge
#Trivia game that reads a plain text file
import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("Press the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answer = next_line(the_file)
        answers.append(answer)
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    print("\n\n\t\tWelcom to Trivia Challenge!")
    print("\t\t", title, "\n")
            
def main():
    the_file = open_file('test_contents.txt', 'r')
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print("\n", category)
        print(question)
        for i in range(4):
            print(answers[i])
        user_ans = input("ENTER THE LETTER OF THE CORRECT ANSWER: ")
        if user_ans.upper() == correct:
            print("Nice! +1 point")
            score += 1
        else:
            print("Pathetic, you get nothing")
        print(explanation)
        print("Score is: ", score)
        category, question, answers, correct, explanation = next_block(the_file)
    the_file.close()
    print("Goodbye")
    print("Score is: ", score)
    input("...")

main()
