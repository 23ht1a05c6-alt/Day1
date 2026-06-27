


'''

balance = 1000
withdraw = int(input("enter a withdraw amount:"))
if withdraw <= balance:
    balance = balance - withdraw
    print("balance remaing")
else:
    print("invalid balance") 


'''       


'''
n = int(input())

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

'''


'''
Start with fact = 1
Multiply fact by each number from 1 to n
Print the final result

for i in range(1, n+1):
1 = starting value
n+1 = ending value is not included in range()
Example






n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

'''

def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
n = int(input("enter a number")) 
if is_prime(n):
    print("prime number")
else:
    print("not a prime")
