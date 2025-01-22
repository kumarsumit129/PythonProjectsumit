#create string variable
#Examole 1: ways of creating string variable
from tkinter.font import names

s="welcome"
s1='welcome'
s2=str('welcome')
s3=str("welcome")

#creating empty string variables
name=""
name1=''
name2=str()

#Examole 2: How th string memories changed
# mutable- cannot change the value of variable
#immutable- can change the value of variable
#string is immutable


str1="welcome"
print(id(str1))

str1=str1+"to python"
print(id(str1))

#if the value is changed after updation then it is immutable

#Examole 3: + and * with string
str1="welcome"
print(str1+"programming")
print(str1*3)

#Example4 : slicing []
#starting index 0
#ending index 1
str9="welcome"
print(str[1:3])
