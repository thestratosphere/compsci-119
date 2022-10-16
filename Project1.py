#COMPSCI 119.01 - Project 1 - Jacqueline "Nora" Cole - Date Submitted: October 16th, 2022

#Start
#Prelude before the loop
import math
degreesRawer = input("What is the degrees?: ")
degreesRaw = float(degreesRawer)
degrees = (degreesRaw % 360) #Extra Credit #1
x = math.radians(degrees)
sine = 0.0
cosine = 0.0
exponent = 0
xpower = 1.0
factorial = 1.0
MoreToDo = True

#The loop
while MoreToDo:
    if MoreToDo == True:
        term = (xpower/factorial)
        if ((exponent//2)%2) == True:
            term = -term
        else:
            pass
        if (exponent%2) == True:
            sine = (sine + term)
        else:
            cosine = (cosine + term)

        print(f"{exponent}, {term:.4f}, {sine:.4f}, {cosine:.4f}") #Extra Credit #2
        xpower = (xpower * x)
        exponent = (exponent + 1)
        factorial = (factorial * exponent)
        MoreToDo = abs(term) >= 1.0e-15

#Exiting the loop
print(f"\nThe calculated Sine is: {sine} \nwhile the calculated Cosine is: {cosine}") 
sinPy = math.sin(x) #Extra Credit #3
cosPy = math.cos(x) #Extra Credit #3
print(f"Whereas the Python Sine is: {sinPy} \nand the Python Cosine is: {cosPy}\n") #Extra Credit #3
#Stop