##imports & test
import numpy as np
print("Hello World!")
print("This program makes an array given two numbers.")
print("First, input the number of columns you want.")
print("Then, input the number of elements you need")
print("Restart the array by typing 'y'. Anything else will end the program.")

##variables
restart = "y"
        
#rearange in lines of 5
while restart == "y":
    y = int(input("Enter the # of rows you want to divide the interger into: "))
    x = int(input("Enter an interger divisable by "+str(y)+": "))
    if x%y == 0:
        a = np.arange(x).reshape(int(x/y), y)
        print(a)
        restart = input("restart? y/n: ")
    else:
        print("That interger is not divisable by "+y)

##quit the program   
if restart != "y":
    quit()
    
