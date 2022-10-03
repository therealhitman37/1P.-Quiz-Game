#In the old code there is sth not right, everytime it shows the right answer before asking you to play again, that is really pointless
#so i change the code a litte bit, now if you answer yes to play again, it doesn't show anything, if the answer is no then it shows the question's right answers

print("Welcome to our game!")

questions = {"Where is the game's owner from: ":"A",
            "Which one is the capital of Vietnam: ":"B",
            "Which one is the biggest city in Vietnam: ":"A",
            "Which one is the cleanest city in Vietnam? ": "D"}

options = [["A.Vietnam","B.Germany","C.China","D.Othher Planet"],
            ["A.HCMC","B.Hanoi","C.Vinh","D: Da nang"],
             ["A.HCMC","B.Hanoi","C.Vinh","D: Da nang"],
              ["A.HCMC","B.Hanoi","C.Vinh","D: Da nang"]]

def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print(key)

        for i in options[question_num]:
            print(i)

        guess = input("Please enter your answer here! A,B,C or D? ").upper()
        guesses.append(guess)
        
        correct_guesses += check_guesses(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)


def check_guesses(answers,guess):
    if answers == guess:
        print("Correct")
        return 1

    else:
        print("Wrong")
        return 0



def play_again():
    response = input("Do you want to play one more game? Yes or No? ").lower()
    if response == "yes":
        return True

    else:
        return False

def display_score(correct_guesses,guesses):
    print("------")
    print("Result")
    print("------")

    print("Your answers: ",end = "")
    for i in guesses:
        print(i, end = " ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is "+ str(score)+ "%")


new_game()

while play_again():
    new_game()


print("Correct answers: ",end = " ")
for i in questions:
    print(questions.get(i), end = " ")
print()

print("Byeeeeee!")
