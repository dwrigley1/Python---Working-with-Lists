''' this script is to give examples on how to use the pop() function'''

myList = [1,2,3,4,5]
print(myList) # prints the whole list as originally typed

myList.pop() # removes last item in list
print(myList)

while len(myList):
    print(myList.pop()) # removes items from the end of the list

print(myList) # prints an empty list because of the previously used pop() function

