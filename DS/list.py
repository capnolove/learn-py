# list can be written by a lot of comma-seperated items in square bracket
# items in list don't need to be the same type

list1 = ['a', 'b', 1000, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

# accessing value
print ("list1[0]: ", list1[0]) # it will print the value for index 0
print ("list2[1:5]: ", list2[1:5]) # it will print the value from index 1 to 4

# update list
list1[0]=1 # replace value in index 0
list1.append(5000) # append(value) means add a value into the last index of the list

# remove list
list1.remove (1000) # remove a specific value inside the list
del list2[3] # remove a value within its index

# few more basic operations for list
print (len(list1)) # print the length of list1
print (list1+list2) # print the concatenation list between list1 and list2
for x in list1: # for loop 
    print(x)