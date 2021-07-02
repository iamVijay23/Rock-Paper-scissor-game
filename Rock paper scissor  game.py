#project based on the rock paper scissor game:



import random #importing the random module
option= ["rock","paper","scissor"] #giving the options
computer=random.choice(option)
user=False # its means the user value is empty for now
user_scr=0 # intializing the value to starting value is 0
cpu_scr=0
run = True
while run:  # here is we intialize the flag variable which run the loop until the condition is true
    user = input("choose the option:")  # for user it will provide the option by itself
    # we can also use the random.choice(option) instead of input but we have to pass the End in the list
    if user == computer:
        print("It s TIE play again")
    elif user == "rock":
        if computer == "paper":  # here we use the nested if
            print("Computer won this round")
            user_scr += 1  # here if the condition wiil be true then the value of user_scr incremented by 1
        else:
            print("User won the round ")
            cpu_scr += 1  # here if the condition wiil be true then the value of cpu_scr incremented by 1
    elif user == "paper":
        if computer == "scissor":
            print("Computer won this round")
            user_scr += 1
        else:
            print("User won the round ")
            cpu_scr += 1
    elif user == "scissor":
        if computer == "rock":
            print("Computer won this round")
            user_scr += 1
        else:
            print("User won the round ")
            cpu_scr += 1
    elif user == "End" or "end":  # when user type the end loops stop there and it will print the score
        print("printing the score:")
        print(f"Computer score is:{cpu_scr}")  # here we used f string method we can  also use the format string
        print(f"User score is:{user_scr}")
        break











