'''
for num in range(1,101):
    is_prime= True
    for i in range(2, num):
        if num % i ==0:
            is_prime = False
            break
    if is_prime:
            print(num)



n =int(input('enter a number'))
rev = 0
t = n
while n>1:
    r = n%10
    rev= rev + r*r*r
    t = n//10
if rev == t:
    print("Amstrong Number")  
else:
    print("Not an Amstrong Number")      



def sum(a,b):
    c=a+b
    print(c)
sum(10,20)    





#count digts
#count the of digits i anumber
n = int(input('enter the number'))
count = 0
while n>0:
    count = count+1
    n = n // 10
print('digit=',count)



n = int(input('enter a number'))
s = 0
while n>0:
    s +=  n%10
    n = n // 10
print("sum=", s)
  
 
reverse number
reverse the digit of a number
ex:123-321

n = int(input('enter a number'))   
rev = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n = n//10
print('reverse=', rev)    



n = int(input('enter a nuber'))
a = 0
b = 1
for i in range(1, n+1) :
    print(b, end="")
    c = a+b
    a = b
    b = c
  



n = int(input('enter a number'))
temp = n
sum = 0
while n>0:
    digit = n%10 # sum= sum=digit
    sum = sum+digit **4
    n = n//10
if temp == sum :   
   print('amstong no') 
else:
    print('not a amstrong')   




n = int(input('enter a number'))
fact = 1
for i in range(1, n+1):
    fact= fact+1
print('factorial=',fact) 
'''


