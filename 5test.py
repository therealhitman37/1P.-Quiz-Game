questions = {"Where are you from? ":"A",
            "Is the earth rough? ": "B",
            "Do you feel happy in your life? ": "C",
            "What auto brand do you want to buy? ": "D"}

options = [["A.Vietnam","B.Germany","C.The Moon","D.The Sun"],
          ["A.False","B.true","C.Sometimes","D.What is the earth"],
          ["A.Yes","B.No","C.I hate my life so much"],
          ["A.Mercedes","B.Porsche","C.Audi","D.Vinfast"]]

def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 0

  for key in questions:
    print("------")
    print(key)

    for i in options[question_num]:
      print(i)

    guess = input("Please input your answer here: ").upper()
    guesses.append(guess)
      
    correct_guesses += check_answers(questions.get(key),guess)
    question_num += 1

  display_score(correct_guesses,guesses)

def check_answers(answer,guess):
  if answer == guess:
    print("Correct")
    return 1

  else:
    print("Wrong")
    return 0
  

def display_score(correct_guesses,guesses):
  print("-----")
  print("Result")
  print("-----")
  
  print("Correct Answers:  ",end = " ")
  for i in questions:
    print(questions.get(i),end = " ")
  print()

  print("Your answer: ",end  = " ")
  for i in guesses:
    print(i,end = " ")
  print()

  score = int((correct_guesses/len(questions)) *100)
  print("Your score is: "+ str(score) + "%")
  
def play_again():
  response = input("Do you want to play again? Enter Yes to play again, No to give up? ").upper()
  if response == "YES":
    return True
  else:
    return False

new_game()

while play_again():
  new_game()

print("Byeeeeeeeeeeeeeeee")

