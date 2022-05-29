
from select import select
from unittest import result
from helper.addition import add
from helper.division import division
from helper.multiplication import multi
from helper.subtraction import sub

print("Welcome to Simple calculator! Please select one of these options:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    select = input ("Enter selection (1,2,3,4): ")

    if select in ('1','2','3','4'):
        num1 = int(input("enter first number: "))
        num2 = int(input("enter second number: "))

        if select == '1' :
            result = add(num1, num2)
            print(num1, '+', num2, result)
        elif select == '2' :
            result = sub(num1,num2)
            print(num1, "-",num2, result)
        elif select == '3':
            result = multi(num1,num2)
            print(num1, "*",num2, result)
        elif select == '4':
            result = division(num1,num2)
            print(num1, "/",num2, result)
        
        select_next = input("Next calculation? (y/n): ")
        if select_next == "n":
            break
        
        else:
            print("Invalid input, try again!")



