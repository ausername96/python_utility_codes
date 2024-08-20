#importing random module
import random
#taking input of a random num
num=random.choice([i for i in range(0,100001)])
#checking if prime
if num>1:
    factors=[]
    for i in range(1,num+1):
         if num%i==0:
             factors.append(i)
    if len(factors)==2:
         print(f"{num} is a prime number")
    else:
         print(f"{num} is not a prime number")
else:
    print(f"{num} is not a prime number")
