salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7] #We need to make salary lsit
y = '' #Make blank str to save to out output
n = 0 # count loops
for x in salary_list: #for loop
    y += str(round(x*1.3, 2))+' '#adding to blank str values, saving it for output
    n += 1 # count loops
    if n % 3 == 0: # we can see in input, every three values new row, so we use \n
        y += '\n' #start from new row
print('Salary table'+'\n'+y) # make output of y str