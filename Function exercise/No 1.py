def convert_to_days():                      #main function with no parameters

    hour = eval(input("Enter numbers of hours:"))               #Enter statement
    minutes = eval(input("Enter numbers of minutes:"))
    seconds = eval(input("Enter number of seconds:"))
    print("The number of days is:", get_days(hour,minutes,seconds))

def get_days (hour,minutes,seconds):                            #helper function to covert
    days = (hour/24) + (minutes/1440) + (seconds/86400)         #the formula is used to change hour, minutes and seconds to day
    return round(days,4)                                        #built in function with 2 arguments

convert_to_days()