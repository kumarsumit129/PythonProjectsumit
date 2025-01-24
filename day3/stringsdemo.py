#create string variable
#Examole 1: ways of creating string variable
from tkinter.font import names

# s="welcome"
# s1='welcome'
# s2=str('welcome')
# s3=str("welcome")

#creating empty string variables
# name=""
# # name1=''
# # name2=str()

#Examole 2: How th string memories changed
# mutable- cannot change the value of variable
#immutable- can change the value of variable
#string is immutable


# str1="welcome"
# print(id(str1))

# str1=str1+"to python"
# print(id(str1))

#if the value is changed after updation then it is immutable

#Examole 3: + and * with string
# str1="welcome"
# print(str1+"programming")
# print(str1*3)

#Example4 : slicing []
#starting index 0
#ending index 1
# str="welcome"
# print(str[1:3]) #el
# print(str[:6])  #welcome here starting index is 0 by default
# print(str[2:])  #lcome

#print(str[1:-1])  #elcom last 1 char removed

#Example5 : ord() and chr()
# print(ord('A')) #65  #returns the ASCII code
# print(chr(65))  #A   #eturns the character represented number

#Example6: max() min() len()
# print(max("abc")) #c
# print(min("abc")) #a
# print(len("abc")) #3

#Example7: in, not in operators - returns true/false
s='welcome'
# print("come" in s) #True
# print("lome" in s) #False

# print("come" not in s) #False
# print("lome" not in s) #True




#Example8: String comparison
# print("tim" == "tie") #False
# print("free" != "freedom") #True
# print ("arrow" > "aron") #True
# print ("right">= "left") #True
# print ("teeth" < "tee") #False
# print ("yellow" <="fellow") #False
# print ("abc"> "") #True

# Example9 : Testing strings True/False
# s="welcome to python"
# print (s.isalnum()) #False
# print("Welcome".isalpha()) #True
# print("2012".isdigit()) #True
# print("first Number".isidentifier()) #False
# print(s.islower()) #True
# print("WELCOME".isupper()) #True
# print(" ".isspace()) #True


#Example10: Searching for Substrings
# s="welcome to python"
# print(s.endswith("thon")) #True
# print(s.startswith("good")) #False
# print (s.find("come")) #3
# print(s.find("become")) #-1 not found
# print(s.count("t")) #2 #Returns number of occurrences of substring the string



#Example11: Converting String
# s="String in PYTHON"
# s1 = s.capitalize()
# print(s1) #String in python
# s2= s.title()
# print (s2) #String In Python
# s3 = s.lower()
# print(s3) #string in python
# s4= s.upper()
# print(s4) #STRING IN PYTHON
# s5 = s.swapcase()
# print(s5) #STRING IN python
# s6 = s.replace("in", "on")
# print(s6) #STRING on python




#Example12: Reverse a string
#Method1
#s="welcome"
# rev_str=""
# for i in s:
# rev_str=i+rev_str #emoclew
# print("reversed string is: ", rev_str) #emoclew
#Method2


s="welcome"
rev_str=s[::-1] #s[0:7:-1]
print (rev_str) #emoclew
