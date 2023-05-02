import keyboard as key
#Function calc
def Calc():

    iNum1 = 0
    iNum2 = 0

    #Loop for input
    for i in range(2):
        if i == 0:
            iNum1 = int(input(f"Input two numbers. Number {i+1} = "))
        else:
            iNum2 = int(input(f"Input two numbers. Number {i+1} = "))

    sArith = input("Input arithmetic method in the form of (+, -, *, /) " )

#Series of if and elif statements to check operator and do calc
    if sArith == "+":
        rSum = iNum1 + iNum2
        print(f"The awnser is: {rSum}")

    elif sArith == "-":
        rSum = iNum1 - iNum2
        print(f"The awnser is: {rSum}")

    elif sArith == "*":
        rSum = iNum1 * iNum2
        print(f"The awnser is: {rSum}")

    elif sArith == "/":
        rSum = iNum1 / iNum2
        print(f"The awnser is: {rSum}")
    else:
        print("The character entered is not valid. Please try again ")
        Calc()

#Running calc function
Calc()

#So program does not close until q is pressed 
key.wait("q")
