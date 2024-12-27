mins = float(input())# Input float minutes
if mins < 0: #Branching
    print("error")
else:#Branching
    if mins/50.0 == mins//50.0 and (mins - 50) > 0:#Branching check if mins - 50 > 0
        print("Ваш сумма сплати пакету за місяць: "+str(100+(mins-50))) #Виводимо
    elif (mins-50.0)//50 <= (mins-50.0)/50 and (mins - 50) > 0:#Branching
            print("Ваш сумма сплати пакету за місяць: "+str(100+50*((mins-50.0)//50+1))) #Можна було додати до хвилин 50, але лінь думати, виводимо
    else:#Branching
         print("Ваш сумма сплати пакету за місяць: 100") #Виводимо