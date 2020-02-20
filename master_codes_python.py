#!/usr/bin/python3
#output
print("give me a bottle of rum!")
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # two stars are used for exponentiation (2 to the power of 16)
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
        # it returns only the quotient of the division (i.e. no remainder)
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder of the left value divided by the right value
#------------------------------------------------------------------------------
#input
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')

a = input()
b = input()
s = a + b
print(s)

irst = 5
second = 7
print(first * second)

a = int(input())
b = int(input())
s = a + b
print(s)

# you can use single or double quotes to define a string
first = '5'
second = "7"
print(first * second)

#Variables declaration
variable_A = 0;
variable_B = 0;
variable_C = 0;
delta_result = 0;
modulo_result = 0;
x1_result = 0;
x2_result = 0;
result = 0;
#Variables ok!


print("Insert the value of A\n"); #Insert value of a
variable_A =int(input()) #Input a
print("Insert the value of B\n"); #Insert value of b
variable_B = int(input()) #Input b
print("Insert the value of C\n"); #Insert value of c
variable_C = int(input()) #Input c
#First stage input ok!
print(variable_A + variable_B + variable_C)

#-----------------------------------------------------------------------------
#IF statement simple
if( statement ):
    print("User input is Number ")
else:
    print("User input is string ")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")



 # In this program,
# we check if the number is positive or
# negative or zero and
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s)



#!/usr/bin/python

var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"
  #---------------------------------------------------------------------------
Radice QUADRATA
# Python3 program to demonstrate the
# sqrt() method

# import the math module  
import math

# print the square root of  0
print(math.sqrt(0))

# print the square root of 4
print(math.sqrt(4))

# print the square root of 3.5
print(math.sqrt(3.5))
