# ВАШ КОД ТУТ
#import sys 
#sys.setrecursionlimit(24)
def cons(head, tails=[]):#Щоб при 1 ь=було все ок
    return [head]+tails#Метод проб та помилок
# ПЕРЕВІРКА

l = cons(3, cons(2, cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')