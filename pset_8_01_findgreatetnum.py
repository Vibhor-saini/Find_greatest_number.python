num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

def max(num1,num2,num3):

    if (num1>num2):                # #
        if(num1>num3):      # # #    #
          return num1           #    #
        else:                   #    #
             return num3    # # #  # #
    else:
        if(num2>num3):
            return num2
        else:
             return num3
m = max(num1,num2,num3)
print("the maximum number is " + str(m))