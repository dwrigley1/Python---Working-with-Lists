my_list = [1, 2, 3, 4, 5]
print(my_list) # prints the list normally
print(*my_list) # prints the individual elements of the list without the brackets & commas

my_list.append(6) # appends a new element to the list
print(my_list)

my_list.remove(6) # removes an element from the list
print(my_list)

my_list.pop(2) # removes an element from the list at a specific index
print(my_list)

my_list.copy # copies the list
print(my_list)

my_list.clear() # clears the list
print(my_list) # prints an empty list

my_list.reverse() # reverses the order of the list
print(my_list) # prints the reversed list

## OOPS ##
## we need to declare a new list ##

my_list = [1, 2, 3, 4, 5]

my_list.reverse() # reverses the order of the list
print(my_list) # prints the reversed list

## you may also use the sort method & set the reverse parameter to True to sort the list in descending order ##

my_list.sort(reverse=True) # sorts the list in descending order
print(my_list)

my_list.sort() # sorts the list in ascending order
print(my_list)

## let's declare a new list so it is easier to see how the count() method works##

my_list = [1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5,]
x = my_list.count(1) # counts the number of occurrences of an element in the list
print(x)

y = my_list.index(5) # returns the index of the first occurrence of an element in the list
print(y)

my_list.insert(0, 0) # inserts an element at a specific index in the list 
print(my_list) # the first argument is the index where the element should be inserted, the second argument is the element itself

my_list.extend([6, 7, 8]) # extends the list by adding multiple elements to it
print(my_list)