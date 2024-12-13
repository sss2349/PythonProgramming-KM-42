from math import sqrt
def triangle_ineq(func):
    def func1(x, y, z):
        if x+y > z and y+z>x and z+x>y:
            return func(x, y, z)
        else:
            return "Not correct values for triangle inequality"
    return func1
def check(x, y, z):
    if x>0 and y>0 and z > 0:
        return True
    return False
@triangle_ineq
def area_calculation(x, y, z):
    if check(x, y, z) == True:
        p = (x+y+z)/2
        S = sqrt(p*(p-z)*(p-x)*(p-y))
        return 'Square of triangle is '+str(round(S, 2))
    else:
        return 'Not correct values >0'
print(area_calculation(4, 5, 6))
print(area_calculation(4, 5, 10))
print(area_calculation(4, 5, -1))
print(area_calculation(10, 5, 6))