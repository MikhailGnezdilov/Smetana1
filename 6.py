A = []
for i in range (0,15):
    x=int(input())    
    A.append(int(input())) 
    
print("Старый массив A:")
print(A)

print('Исходный массив A')
print(A)

A.reverse()
print('Новый массив A')
print(A3)

s=0
for i in range(len(A)):
     s += A[i]
     
print('s =', s)
