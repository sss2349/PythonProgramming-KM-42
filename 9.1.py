import numpy as np
import itertools

def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix
#print(random_matrix(3)) [[7, 2, 5], [7, 3, 7], [2, 7, 0]]
#Example of using permutations() method
def list_p(m): # Робимо функцію Ліст яка зробить глобальну змінну х(список перестановок) та віддасть матрицю в наступну функцію
    global x #глобал змінна
    x = itertools.permutations(range(len(m))) #список перестановок
    return m #повертаємо матрицю
def mult(m): #Робимо функцію яка буде обчислювати мінори методом перестановок
    y = [] #Робимо список, щоб всі мінори можна було зібрати і додати
    for p in x: # Вибираємо перестановки зі списку перестановок по черзі
        z = 1 #Має стояти саме тут, значення має відкидуватись до одного, кожної нової перестановки
        for i in range(len(m)): #беремо числа від одного до порядка матриці
            z = z*m[i][p[i]]# перемножаємо кожні наступні елементи н разів(де н порядок матриці)
        inv = 0 #поки кількість інверсій перестановок 0
        for k in range(len(p)): #Робимо цикл фор перебираємо перестановки 1, 2, 3...
            for l in range(k + 1, len(p)): #Від числа перестановки до її довжини
                if p[k] > p[l]: #Якщо перестановка елемент К > елмента Л то додаємо 1
                    inv += 1
        if inv % 2 :# перевіряємо на парнітсь
            y.append(z*(-1))#знак мінус
        else:#Інакше в нас знак +
            y.append(z*(1))#Додаємо кожен елемент z
    return y#Повертаємо список визначників, добре що є sign, а то я би зробив паунс у вікно
def sum_m(m):# Функція суми, сумуємо елементи(мінори) списку
    return np.sum(m) #Повертаємо
#print(sum_m(mult(list_p([[7, 2, 5], [7, 3, 7], [2, 7, 0]]))))
#print(sum_m(mult(list_p(random_matrix(4)))))