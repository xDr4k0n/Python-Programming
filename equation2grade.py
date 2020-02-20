#!/usr/bin/python3
import math
print("Program to calculate the 2_grade equations...");
variable_A = 0;
variable_B = 0;
variable_C = 0;
delta_result = 0;
modulo_result = 0;
x1_result = 0;
x2_result = 0;
result = 0;
#Variables ok!
print("Insert the value of A\n") #Insert value of a
variable_A =int(input()) #Input a
print("Insert the value of B\n") #Insert value of b
variable_B = int(input()) #Input b
print("Insert the value of C\n") #Insert value of c
variable_C = int(input()) #Input c
#First stage input ok!
if( variable_A == 0 ):
    print("Value of A cannot be 0, re-enter an outher number\n")
    print("Insert the value of A\n") #Insert value of a
    variable_A =int(input()) #Input a
else:
    print("Input is ok \n")
#Check if A is 0
#------------------------------------------------------------------------------
if variable_B == 0 :
    print("Value of B is 0")
    if variable_C == 0:
        print("Error B and c cannot be 0!")
    else:
        print("The equation is incomplete `Pura`!")
        print("b = 0 & c != 0")
elif variable_C == 0 :#B = 1
    print("The equation is incomplete `Spura`!")
    print("b != 0 & c = 0")
else:
    print("The equation is complete !")
    print("b != 0 & c != 0")
#------------------------------------------------------------------------------
delta_result = ((variable_B * variable_B)-(4*variable_A*variable_C));
print(delta_result);
print("TEST REMOVE ME AFTER");
#------------------------------------------------------------------------------
if( delta_result > 0 ):
    #main if statement DELTA
    #TRUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    print("Delta is a Positive Number!")
    print("After calculation Delta is")
    print("bigger than 0\n")
    x1_result = int(-variable_B - int(math.sqrt(delta_result)) / 2 * variable_A);
    x2_result = int(-variable_B + int(math.sqrt(delta_result))/2 * variable_A);
    print("x1 = ", x1_result)
    print("x2 = ", x2_result)
    #--------------------------------------------------------------------------
    #X1 and X2 Done calculation Succesfuly integer numbers
    #------------------------------------------------------------------------------
    #X1 identification
    if x1_result > 0:
        modulo_result = int (x1_result % 2);
        if modulo == 0:
            print("x1 is a PARI POSITIVE number!\n")
        else:
            print("x1 is a IMPARI POSITIVE number!\n")
    if x1_result == 0:
        print("x1 is a NULL NUMBER\n")
    else:
        modulo_result = int(x1_result % 2);
        if modulo_result == 0:
            print("x1 is a PARI NEGATIVE number!\n")
        else:
            print("x1 is a IMPARI NEGATIVE number!\n")


    #---------------------------------------------------------------------------
    #X2 identification
    if x2_result > 0:
        modulo_result = int(x2 % 2);
        if modulo_result == 0:
            print("x2 is a PARI POSITIVE number!\n")
        else:
            print("x2 is a IMPARI POSITIVE number!\n")
    if x2_result == 0:
        print("x2 is a NULL NUMBER\n")
    else:
        modulo_result = int(x2_result % 2);
        if modulo_result == 0:
            print("x2 is a PARI NEGATIVE number!\n")
        else:
            print("x2 is a IMPARI NEGATIVE number!\n")
    #--------------------------------------------------------------------------
else:
    #main if statement DELTA
    print("Delta is a Negativer or NULL!\n")
    if delta_result == 0:
        #if TRUEEEEEEEEEEEEEEEEEEEEEEEE
        print("NO REAL SOLUTION!!!!!!!\n")
        print("Delta NULL!\n")
    else:
        print("After the calculation\n")
        print("Delta is a Negative!\n")
        result = int(-variable_B / 2 * variable_A);
        x1_result = result;
        x2_result = result;
        print("After the calculation\n")
        print("X1 = X2 = \n", result)
        if x1_result > 0:
            modulo_result = int(x1_result %2);
            if modulo_result == 0:
                print("After the calculation\n")
                print("X1 = X2 = PARI POSITIVO\n")
            else:
                print("After the calculation\n")
                print("X1 = X2 = IMPARI POSITIVO\n")
        elif x1_result == 0:
            print("After the calculation\n")
            print("X1 = X2 = NULLLLLLLLLL\n")
        else:
            modulo_result = int( x1_result %2);
            if modulo_result == 0:
                print("After the calculation\n")
                print("X1 = X2 = PARI NEGATIVO\n")
            else:
                print("After the calculation\n")
                print("X1 = X2 = IMPARI NEGATIVO\n")
print("FINE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
