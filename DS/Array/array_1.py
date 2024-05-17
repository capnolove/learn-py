from array import *

# typecode 'i' means integer
# arrayName=(typecode, [value in an array])
a=array('i', [10, 20, 30])

# print array element with index number
print (a[1])

# insert an element into an array
# insert(index, value want to add)
a.insert(4, 50)
for x in a:
    print(x)

# delete an element inside an array
# remove(element)
a.remove(20)
for x in a:
    print(x)


# search (find the index of the element)
print (a.index(10))

# update an element to a given index
a[3]=40
for x in a:
    print (x)
