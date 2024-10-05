print("Введіть дві фрази, перша фраза, друга підфраза")
f1 = set(sorted(str(input()).lower()))
f2 = set(sorted(str(input()).lower()))#Вводимо
f11 = []
f22 = []
f33 = []
for x in list(f2):#Пробіли -
    if x.isalpha()==True:#Розгалуження
        f22.append(x)
    else:#Розгалуження
        pass
for x in list(f1):
    if x.isalpha()==True:
        f11.append(x)
    else:#Розгалуження
        pass
for x in f22:
    if x in f11:#Розгалуження
        f33.append(x)
    else:#Розгалуження
        pass 
if f33==f22:#Розгалуження
    print(set(f11), set(f22), "Так можна скласти")       
else:#Розгалуження
    print(set(f11), set(f22), "Ні не можна скласти")   
