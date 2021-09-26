# Function creation:-
# Built in function and User define function

# Built in function(max- find greater value):-
# Example 1
# a=22
# b=13
# c=max((a,b))
# print(c)

# Example 2(sum- add)
# a=34
# b=77
# c=sum((a,b))
# print(c)

# User defined functions:-
# a=2:
# def my_function():
#     b=a*a
#     print(b)
#     my_function()

def percentage(tot):
    per=tot/500*100
    returne=(per)

def printline():
    print("-----------------------------------")

phy=88
che=90
math=80
hindi=55
eng=88
tot=sum((phy,che,math,hindi,eng))
result=percentage(tot)
print("printline()")
print("Your total number is",tot)
print("printline()")
# print("Your percentage is",round(result,2))  - not run