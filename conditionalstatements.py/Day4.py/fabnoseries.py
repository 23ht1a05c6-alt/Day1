a = 0 #0+1=1
b = 1
n = int(input('enter a number of teerms'))
for i in range(1,n+1):
    c = a+b #a+b = 1 then c = 1
    a = b  
    b = c  #here a=1,b=1
print(c) 




n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

'''

Explanation
Start with a = 0, b = 1
Print a
Update values:
a = b
b = a + b
Repeat n times
First number = 0
Second number = 1
Third number = 0 + 1 = 1
Fourth number = 1 + 1 = 2
Fifth number = 1 + 2 =3
'''