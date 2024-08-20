#import random module
import random
#computing factorial
i=random.choice([i for i in range(0,11)])
#its limit is i=1558
factorial=1
try:
    for j in range(1,i+1):
        factorial*=j
    print(factorial) 
except:
    print("Number error:enter a smaller number")