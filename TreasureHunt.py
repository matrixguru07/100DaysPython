print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇
dir = input(
    "Your are at the cross road. where do you want to go? type \"left\" or \"right\" ? \n"
).lower()
if dir != "left":
    print("Fall into a hole. Game Over ")
else:
    que2 = input(
        "You come to a Lake. There is an island in the middle of the lake. type \"swim \" to swim across. Type \"wait\" to wait for a boat \n"
    ).lower()
    if que2 != "wait":
        print("Attacked By Trout. Game Over:(")
    else:
        door = input(
            "You arrive at the island unharmed. there is a house with 3 Doors. One red, one yellow and one blue. which colour do you choose? \n"
        ).lower()
        if door == "red":
            print("Burned By fire Game Over :(")
        elif door == "blue":
            print("Eaten By beast game over:(")
        elif door == "yellow":
            print("You win!! ")
        else:
            print("Game Over:(")
