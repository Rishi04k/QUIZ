print("Welcome to My QUIZ!")

playing = input("Do you want to play..? ")

if playing.lower() != "yes":
    quit()

print("Okay, Let's play :) ")
score = 0

answer = input("What does RAM stands for ..?  ")
if answer.lower() == "random access memory":
    print('CORRECT! ')
    score += 1
else:
    print("InCORRECT! ")    

answer = input("What does CPU stands for ..?  ")
if answer.lower() == "central processing unit":
    print('CORRECT! ')
    score += 1
else:
    print("InCORRECT! ")    

answer = input("What does ROM stands for ..?  ")
if answer.lower() == "read only memory":
    print('CORRECT! ')
    score += 1
else:
    print("InCORRECT! ")    

answer = input("Printer is a software device..!  (true/false)  ")
if answer.lower() == "true":
    print('CORRECT! ')
    score += 1
else:
    print("InCORRECT! ")    

print ("You got " +  str(score)  + " Questions CORRECT..! ")  
print ("You got " +  str((score / 4) * 100)  + "%.")  