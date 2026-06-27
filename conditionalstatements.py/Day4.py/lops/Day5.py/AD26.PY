

'''

def sum_of_digit(n):
    total = 0
    while n>0:
   
       total = total+(n%10)
       n = n//10
    return total           
 
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
if is_prime("prime number"):
    print("prime number") 
else:
    print("not prime nuber")    

    
    
      