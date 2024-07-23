def strange_list_fun(n): # 
    strange_list = [] # 
    
    for i in range(0, n): # 
        strange_list.insert(0, i) # 
    
    return strange_list

print(strange_list_fun(5))

'''
what does each line actually mean, though? 
'''
# Line 1
# This line defines a new function named strange_list_fun that takes one parameter n.
''''''
# Line 2
# This line initializes an empty list called strange_list.
''''''
# Line 4
# This line starts a for loop that will iterate i from 0 up to, but not including, n
''''''
# Line 5
# Within each iteration of the loop, this line inserts the current value of i at the beginning 
# (index 0) of the strange_list. This means the new value of i is added to the start of the list, pushing all existing elements one position to the right.
''''''
# Line 7
# After the loop has completed, this line returns the strange_list.
''''''
# Line 9
# This line calls the strange_list_fun function with an argument of 5 and prints the result.