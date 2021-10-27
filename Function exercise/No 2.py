def calc_weight_on_planet(weight,surfaceGravity=23.1):                      #function with 2 arguments (weight and surface gravity)

    w = weight / 9.8                                                        #basic formula to caluclate the weight
    m = w * surfaceGravity                                                  #the weight formula times with the default value which is the surface gravity

    print(m)                                                                #print the m value

calc_weight_on_planet(120,9.8)                                              #Enter the demonstrates so the code works
calc_weight_on_planet(120)
calc_weight_on_planet(120,23.1)