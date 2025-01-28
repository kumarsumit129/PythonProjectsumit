#Example1: How to create List
# myList1=[10,20,30,40,50]
# myList2=["apple", "banana", "cheery" ]
# myList3=["apple", 10, "cheery" ]
# mylist=list()
# print(myList1)
# print(myList2)
# print(myList3)
# print(mylist)

#Example2: Accessing items from the list
# #mylist=["apple", "banana", "cherry"] #index start from 0
# print(mylist[0])
# print(mylist [2])
# print(mylist [-1])
# print(mylist[-2])



#Example3: Range of indexes

#mylist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print (mylist [2:5]) #cherry', 'orange', 'kiwi']
#print (mylist [-4:-1]) #'orange', 'kiwi' 'melon']

#Example4: change item value
# mylist=["apple", "banana", "cherry"]
# print(mylist )
# mylist[0]="orange"
# print(mylist ) #["orange", "banana", "cherry"]

#Example5: read the list items using loop

# mylist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for i in mylist:
#     print(i)

# Example6: check if the item is exist in the list or not
# mylist=["apple", "banana", "cherry", "orange"]
#
# if "apple" in mylist:
#     print("yes apple is present")
# else:
#     print("No apple is not present")

# Example7:List Length (counting number of items in a list)
# mylist=["apple", "banana", "cherry"]
# print(len (mylist)) #3
# Example8: Add items append() insert()
# mylist= ["apple", "banana", "cherry",]
# mylist.append("orange")
# print(mylist)

#Example9: remove item from the list #pop()

#mylist=["apple", "banana", "cherry"]
#mylist.pop(0) # here we should specify index not the value
# print (mylist) #['banana', 'cherry']
#del
#mylist=["apple", "banana", "cherry"]
# del mylist[2]
#here del command removes single item based on the index
# print(mylist) #['apple', 'banana']
#clear()
#mylist=["apple", "banana", "cherry"] #mylist.clear()
# print(mylist) #[]