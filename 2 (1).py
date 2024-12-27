x = int(input())#Input int number,its not specified what input
if x >= 0 and x < 60:#Branching
    print("Unsatisfactory")#Printing
elif x >= 60 and x < 65:#Branching
    print("Marginal")#Printing
elif x >= 65 and x < 75:#Branching
    print("Satisfactory")#Printing
elif x >= 75 and x < 85:#Branching
    print("Good")#Printing
elif x >= 85 and x < 95:#Branching
    print("Very good")#Printing
elif x > 95 and x <= 100:#Branching
    print("Excellent")#Printing
else:   #Branching else
    print("Error")#Printing error