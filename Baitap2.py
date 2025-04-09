my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
my_set.add("banana")  
## print(my_set)  ## output: {'banana', 'orange', 'apple', 'cherry'}
my_set.remove("apple") 
if "mango" not in my_set: 
    my_set.add("mango") 
print(my_set) ## output: {'mango', 'banana', 'orange', 'cherry'}