import numpy as np

A=np.genfromtxt('A.txt')

print('Исходный массив A')
print(A)

B=np.genfromtxt('B.txt')
print('Исходный массив B')
print(B)

P=np.genfromtxt('.txt')
print('Исходный массив P')
print(P)

Q=np.genfromtxt('Q.txt')
print('Исходный массив Q')
print(Q)

R=np.genfromtxt('R.txt')
print('Исходный массив R')
print(R)

x = P-R
print ('x =', x)

y = np.dot(B,x)
print ('y =', y)

s = np.dot(y,R)
print ('s =', s)
