dict = {"A":"Newfoundland",
"B":"Nova Scotia",
"C":"Prince Edward Island",
"E":"New Brunswick",
"G":"Quebec", "H":"Quebec", "J":"Quebec",
"K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario",
"R":"Manitoba",
"S":"Saskatchewan",
"T":"Alberta",
"V":"British Columbia",
"X":"Nunavut",
"X":"Northwest Territories",
"Y":"Yukon"}#Робимо словник
print("Введіть поштовий індекс")
x = str(input()).upper()
while (x[0] in dict and x[1].isdigit() == True and x[-1].isalpha() == True and len(x) == 3) == False:
    print("Помилка введіть 3 значний код формату Х0Х")#Перевірка
    x = str(input())
if x[0] == "X":#Розгалуження
    if x[1] == '0':#Розгалуження
        print("Ти знаходишься в сільскій місцевості, Nunavut або Northwest Territories")
    else:#Розгалуження
        print("Ти знаходишься в міській місцевості, Nunavut або Northwest Territories")
else:#Розгалуження
    if x[1] == '0':#Розгалуження
        print("Ти знаходишься в сільскій місцевості,", dict[x[0]])
    else:#Розгалуження
        print("Ти знаходишься в міській місцевості,", dict[x[0]])