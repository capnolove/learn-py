n=int(input())
list=[]
for i in range(0,n):
    ele=int(input())
    list.append(ele)

total=list[0]
for i in range (0,n):
    for j in range (i+1,n):
        if list[i]==list[j]:
            sequence=list[i:j+1]
            if sum(sequence)>total:
                total=sum(sequence)
        

print (total)

