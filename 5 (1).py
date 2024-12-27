x = []
print("Enter int number, how many words you would like to store")
n = int(input())
for i in range(n):
    print("Enter word")
    x.append(input()) # If we have 4 list vakues input
y = '' # Need to save and output as str
n = 0 #need to count loops
for i in x: #for loop
    if n == (len(x)-2): # need to break and make output
        print(y+x[-2]+' ' +'and '+x[-1]) #maek output print
        break #break
    y += i+', '#add to our str lsit elements
    n += 1 #count loops