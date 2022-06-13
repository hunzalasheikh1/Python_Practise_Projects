print("Welcome to my computer quiz")

playing = input("do you want to play? ")

if playing.lower() != "yes":  
    quit()
    
print("okay lets play: ")

score = 0




answer = input("What does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")
    
    
answer = input("What does GPU stands for ?")
if answer.lower() == "graphics processing unit":
    print("correct")
    score+=1
else:
    print("incorrect")
    
answer = input("What does RAM stands for ?")
if answer.lower() == "random access memory":
    print("correct")
    score+=1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + str((score/3) *100) + "%.")