from math import factorial
def binom1(n):
    def binom(n1):
        for t in range(n1+1):
            s = ''
            for k in range(t+1):
                y = str(int(factorial(n1)/(factorial(n1-k)*factorial(k))))
                s = s+y+' '
        return s
    list1 = []
    for x in range(n+1):
        list1.append(binom(x)) 
    for t in list1:
        yield t   
bin = binom1(5)
print(bin)
print(next(bin))
print(next(bin))
print(next(bin))
print(next(bin))
print(next(bin))
print(next(bin))