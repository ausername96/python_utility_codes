n=6
d1=0
d2=1
try:
    for j in range(1,n+1):
        fibonacchi_seq=d2+d1
        d1=d2
        d2=fibonacchi_seq
    print(fibonacchi_seq) 
except:
    print("Number error:enter a smaller number")