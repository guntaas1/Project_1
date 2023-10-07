
def myAdd(num1 ,num2):   #function for Addition
    total = num1 + num2
    return total

def mySub(num1 ,num2):   #function for Subtraction
    total = num1 - num2
    return total

def myMul(num1 ,num2):   #function for Multiplication
    total = num1 * num2
    return total

def myDiv(num1 ,num2):   #function for Division
    total = (num1 / num2)
    return total

def check_operator(opr_): # this function is used to check whether the input is operator
    opr_list = ['/','-','+','*']
    x = False
    for opr in opr_list:
        if opr_ == opr:
            x = True
    return x

def check_number(user_input): #this function is used to check whether the input is a number
    try:
        number = float(user_input)
        if number.is_integer():
            return True
        else:
            return False
    except ValueError:
        return False

def main(): 
    def_list = ["first" , "second" , "third"]
    num_list = []                                #this is an empty list of numbers
    opr_list = []                                # this is an empty list of operators
    i = 0
    j = 0
    print("Please enter a number.")
    while i < 3:                       #this loop checks if the input is a number and then appends to the number list
        user_input_num = input("Enter the " + def_list[i] + " number: ")
        if check_number(user_input_num) == True:
            num_list.append(int(user_input_num))
            i = i + 1
        else:
            print("Try again.")
    print()
    print("Please enter a operator.")
    while j < 2:                        #this loop checks if the input is a operator and then appends to the operator list
        user_input_opr = input("Enter the " + def_list[j] + " operator: ")
        if check_operator(user_input_opr) == True:
            opr_list.append(user_input_opr)
            j = j + 1
        else:
            print("Try again.")
