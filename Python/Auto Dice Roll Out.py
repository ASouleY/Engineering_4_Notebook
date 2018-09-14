#Auto Dice Roll Out
#Writen by Sam Livingood and Aden Young
#EnterVal=0



import random

print ("Automatic Dice Roller")

repeat = True

while repeat:
    print("you rolled",random.randint(1,6))
    print("Do you want to roll out? (press y to roll again, anything else to shut down)")
    repeat = "y" in input()
else:
    print('Thanks for Rolling')
    
