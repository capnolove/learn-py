# each key in dictionary will be separated by a colon (:)
# items are separated by comma (,)
# empty dictionary is written by {}
# keys must be a data type such as strings, numbers or tuples

# declare a dictionary
dict={"Name":"Laptop", 'Color': ["red","blue"]}

# accessing dictionary items
print (dict["Color"])
print (dict["Name"])

dict["Color"]="red", "blue", "purple" # update existing entry
dict["Brand"]="Dell"                  # add new entry

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary