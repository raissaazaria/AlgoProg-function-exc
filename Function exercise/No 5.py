def convert_temp():
    f = eval(input("Enter a temperature in Fahrenheit:"))
    c = 5/9 * (f-32)
    print("The temperature in Fahrenheit is:", f)
    print("The temperature in Fahrenheit is:", c)
    return c

def convert_to_kelvin():
    x = convert_temp()
    k = x + 273.15
    print("The temperatuure in Kelvin is:", k)

    convert_to_kelvin()