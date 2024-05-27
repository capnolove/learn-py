hash_set=["Andy", "Bob", "Clora", "David", "Edward"]
my_hash_set = [None,None,None,None,None,None,None,None,None,None]

def hash_function(val): # hashing function
    sum = 0
    for char in val:
        sum = sum + ord(char) # unicode val of each char 

    return sum % 10

def contains(name):
    index = hash_function(name)
    return hash_set[index] == name
    





print (contains("David"))