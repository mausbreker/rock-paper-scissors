import random

while True:
    my_answer = input("Choose rock, paper or scissors. Type quit to exit! ")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print(f"You typed {my_answer}. Please choose the correct answer. Try again!")
        continue
    
    com_answer = random.choice(["rock", "paper", "scissors"])
   
    print(f"You chose {my_answer}.")
    print(f"The computer chose {com_answer}.")

    if my_answer == com_answer:
        print(f"It's a tie! Play again...")
        continue

    elif my_answer == "rock" and com_answer == "scissors":
        print("You WIN!")
        break
    
    elif my_answer == "paper" and com_answer == "rock":
        print("You WIN!")
        break

    elif my_answer == "scissors" and com_answer == "paper":
        print("You WIN!")
        break

    else:
        print("You lose! Try again.")