import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(
    input("What do you choose? 0 for rock, 1 for paper or 2 for scissors\n"))

com_choice = random.randint(0, 2)

if choice > 2 or choice < 0:
    print("Invalid input")
else:
    li = [rock, paper, scissors]
    print("Your choice: \n")
    # print(choice)
    print(li[choice])
    print("Computer's choice: \n")
    # print(com_choice)
    print(li[com_choice])

    if com_choice == choice:
        print("Its a tie")
    else:
        if choice == 0 and com_choice == 1:
            print("you lose")
        elif choice == 1 and com_choice == 2:
            print("You lose")
        elif choice == 2 and com_choice == 0:
            print("You Lose")
        elif com_choice == 0 and choice == 1:
            print("you Win")
        elif com_choice == 1 and choice == 2:
            print("You Win")
        elif com_choice == 2 and choice == 0:
            print("You Win")
