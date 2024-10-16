from math import sqrt 
try:
    a = float(input())
    b = float(input())
    c = float(input())
except ValueError:
    print("Введіть числа, а не що ви хочете")
except FloatingPointError:
    print("Введіть не занадто великі числа з плавоючою комою, а не що ви хочете")
except KeyboardInterrupt:
    print("Не пресуй клавіатуру коли вводиш дані")
except NameError:
    pass
try:
    D = sqrt(b**2-4*a*c)
except ValueError:
    print("Корнів немає Д<0")
except KeyboardInterrupt:
    print("Не пресуй клавіатуру коли вводиш дані")
except FloatingPointError:
    print("Введіть не занадто великі числа з плавоючою комою, а не що ви хочете")
except NameError:
    pass
try:
    print((-b+D)/(2*a))
    print((-b+D)/(2*a))
except ZeroDivisionError:
    print("На нуль ділити не можна")
except KeyboardInterrupt:
    print("Не пресуй клавіатуру коли вводиш дані")
except FloatingPointError:
    print("Введіть не занадто великі числа з плавоючою комою, а не що ви хочете")
except NameError:
    pass
