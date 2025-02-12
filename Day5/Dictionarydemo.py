
#cxumpcel. creating dictionary
#mydic={101: "x", 102: "y", 103: "z"}
# print(mydic) #{101: 'x', 102: 'y', 103: 'z'}


#Example2: access items from dictionary
#mydic={
#"brand": "Hyudai",
#"model": "110",
#"year": 2021
#}
#print(mydic["brand"]) # Hyudai
#print (mydic ["model"])#10


# using get()
#print(mydic.get("brand")) #Hyudai

#Example3: change values in dictionary


# mydic = {
#     "brand": "Hyudai",
#     "model": "110",
#     "year": 2020
# }
#
# print(mydic)   # {'brand': 'Hyudai', 'model': '110', 'year': 2020}
# mydic["year"]=2021
# print(mydic)   #{'brand': 'Hyudai', 'model': 'i10', 'year': 2021}



#Example4: reading items from dictionary using loop
# mydic= {
#    "brand": "Hyudai",
#     "model": "110",
#     "year": 2020
# }
# for i in mydic:
#     print(i) # prints only keys from dictionary
# for i in mydic.values():
#         print(i)  # prints only values from dictionary

 #Example5: check key is exist in dictionary or not
# mydic = {
#     "brand": "Hyudai",
#     "model": "110",
#     "year": 2020
# }
#
# if "model1" in mydic:
#     print("exist")
# else:  # Removed extra indentation before 'else'
#     print("not exist")
#
# print("model" in mydic)  # True




#Example6: find number of items in dictionary
# mydic = {
#     "brand": "Hyudai",
#     "model": "110",
#     "year": 2020
# }

print(len(mydic))  # Output: 3

#Example7: Adding items to dictionary
# mydic = {
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
# }

# mydic["color"] = "red"
#
# print(mydic) #{'brand': 'Hyudai', 'model': '110', 'year': 2020, 'color': 'red'}


#Example8: Remove item from dictionary

#
# mydic = {
#     "brand": "Hyudai",
#     "model": "110",
#     "year": 2020
# }

# Using pop() method to remove an item
# mydic.pop("year")
# print(mydic)  # Output: {'brand': 'Hyudai', 'model': '110'}


# del mydic["year"]
# print(mydic)  # Output: {'brand': 'Hyudai', 'model': '110'}

#del mydic
#print(mydic) #Name error

# mydic.clear()
# print(mydic) #{}


# Example9: copying dictionary
mydic1 = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2020
}

# Using copy() method to create a new dictionary
mydic2 = mydic1.copy()

# Print copied dictionary
print(mydic2)


