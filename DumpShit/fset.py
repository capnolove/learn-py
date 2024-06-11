from math import*

def cp(n):
    tf=0
    for i in range (1, n+1):
        if i*i==n:
            tf=1
            break
    return tf
        

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def subset(n):
    return 2**n

n=int(input())
total=0
for i in range (1, n+1):
    if cp(i)==1:
        for j in range (0,i-1):        
            total=total+(factorial(i-2)/(factorial(j)*factorial(i-2-j)))

print (trunc(int(subset(n)-total)))

