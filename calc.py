def myAdd(num1 ,num2):              #function for Addition
    total = num1 + num2
    return total                    #this line is to return the total of the above lines

def mySub(num1 ,num2):              #function for Subtraction
    total = num1 - num2
    return total                    #this line is to return the total of the above lines

def myMul(num1 ,num2):              #function for Multiplication
    total = num1 * num2
    return total                    #this line is to return the total of the above lines

def myDiv(num1 ,num2):              #function for Division
    total = (num1 / num2)
    return total                    #this line is to return the total of the above lines

def check_operator(opr_):           # this function is used to check whether the input is operator
    opr_list = ['/','-','+','*']    # this list is for the checking the user input opertor
    x = False
    for opr in opr_list:
        if opr_ == opr:
            x = True
    return x

def check_number(user_input):       #this function is used to check whether the input is a number
    try:
        number = float(user_input)
        if number.is_integer():
            return True
        else:
            return False
    except ValueError:
        return False

def main(): 
    def_list = ["first" , "second" , "third"]   #
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

    print()                                         #these lines shows for showing what the user has given us.
    print("You input is:")
    print(num_list[0] , opr_list[0] , num_list[1] , opr_list[1] , num_list[2])
    print()

    if ((opr_list[0] == '/') and (opr_list[1] == '/')):                                     #this line checks for((num1/num2)/num3)
        print("Your output is:" , int(myDiv(myDiv(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '/') and (opr_list[1] == '*')):                                   #this line checks for((num1/num2)*num3)
        print("Your output is:" , int(myMul(myDiv(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '/') and (opr_list[1] == '+')):                                   #this line checks for((num1/num2)+num3)
        print("Your output is:" , int(myAdd(myDiv(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '/') and (opr_list[1] == '-')):                                   #this line checks for((num1/num2)-num3)
        print("Your output is:" , int(mySub(myDiv(num_list[0],num_list[1]),num_list[2])))

    elif ((opr_list[0] == '*') and (opr_list[1] == '/')):                                   #this line checks for((num1*(num2/num3))
        print("Your output is:" , int(myMul(num_list[0],myDiv(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '*') and (opr_list[1] == '*')):                                   #this line checks for((num1*num2)*num3)
        print("Your output is:" , int(myMul(myMul(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '*') and (opr_list[1] == '+')):                                   #this line checks for((num1*num2)+num3)
        print("Your output is:" , int(myAdd(myMul(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '*') and (opr_list[1] == '-')):                                   #this line checks for((num1*num2)-num3)
        print("Your output is:" , int(mySub(myMul(num_list[0],num_list[1]),num_list[2])))

    elif ((opr_list[0] == '+') and (opr_list[1] == '/')):                                   #this line checks for((num1+(num2/num3))
        print("Your output is:" , int(myAdd(num_list[0],myDiv(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '+') and (opr_list[1] == '*')):                                   #this line checks for(num1+(num2*num3))
        print("Your output is:" , int(myAdd(num_list[0],myMul(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '+') and (opr_list[1] == '+')):                                   #this line checks for(num1+num2)+num3)
        print("Your output is:" , int(myAdd(myAdd(num_list[0],num_list[1]),num_list[2])))
    elif ((opr_list[0] == '+') and (opr_list[1] == '-')):                                   #this line checks for(num1+num2)-num3)
        print("Your output is:" , int(mySub(myAdd(num_list[0],num_list[1]),num_list[2])))

    elif ((opr_list[0] == '-') and (opr_list[1] == '/')):                                   #this line checks for(num1-(num2/num3))
        print("Your output is:" , int(mySub(num_list[0],myDiv(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '-') and (opr_list[1] == '*')):                                   #this line checks for(num1-(num2*num3))
        print("Your output is:" , int(mySub(num_list[0],myMul(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '-') and (opr_list[1] == '+')):                                   #this line checks for(num1-(num2+num3))
        print("Your output is:" , int(mySub(num_list[0],myAdd(num_list[1],num_list[2]))))
    elif ((opr_list[0] == '-') and (opr_list[1] == '-')):                                   #this line checks for((num1-num2)-num3)
        print("Your output is:" , int(mySub(mySub(num_list[0],num_list[1]),num_list[2])))

if __name__ == '__main__':
    main()