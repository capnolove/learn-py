from math import*
def find_trail_zero (n):
    count=0
    while (n>=5):
        n=n/5
        count=count+n
    return trunc(count)

print(find_trail_zero(int(input())))