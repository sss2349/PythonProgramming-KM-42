# ВАШ КОД ТУТ
def sum(lst):
    if not lst:#якщо пустий
        return 0 #Щоб до суми +0 нан не вийде
    return lst[0]+sum(lst[1:])
# ПЕРЕВІРКА
l = [3, 2, 1]
print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')