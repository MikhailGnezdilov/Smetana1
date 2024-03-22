from math import sqrt
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))
u=1+min((x+y+z)/ max(y,z),x*y*z)
print (u)
