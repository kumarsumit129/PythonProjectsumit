
#Example1
# global_var=20 # global variable
#
# def func():
#
#local_var=10 # local variable
#
#print (local_var)
#
#print (global_var)
#
# func()
#
# #print (local_var) # invalid bcoz local_var is local varaible of func()
# print(global_var) # valid bcoz global_var is global variable

#(Example2)
xy=100 # global variable

def cool():
    xy=200 #global variable
    print(xy)
cool()

