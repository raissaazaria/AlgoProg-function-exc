def calc_new_height():                                              #Input function with no parameters
    w = eval(input("Enter the current width:"))                     #Input statements
    h = eval(input("Enter the current height:"))
    w2 = eval(input("Enter the desired width:"))
    while w2 > w:                                                  #desire width have to be smaller than current width, if bigger user needs to re-enter
        w2 = eval(input("Current width is bigger than desire width, re-enter width:"))

    a = w / w2                                                      #Enter the formula to find scale and than divide the result with first result
    b = h / a
    print("The corresponding height is:",b)                        #print the results

calc_new_height()

