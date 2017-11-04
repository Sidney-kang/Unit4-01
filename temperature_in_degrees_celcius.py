# Created by : Sidney Kang
# Created on : 26 Oct. 2017
# Created for : ICS3UR
# Daily Assignment - Unit4-01
# This program converts the temperature in degrees celcius to degrees fahrenheight

def temperature(temperature_celcius):
    temperature_fahrenheit = (9.0/5.0) * temperature_celcius + 32
    print("The temperature in degrees fahrenheit is: "+ str(temperature_fahrenheit) + "F")
    
temperature_celcius = raw_input("Enter a temperature in degrees celcius: ")
temperature_celcius = float(temperature_celcius)
temperature(temperature_celcius)
