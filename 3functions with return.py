#define a funtion named 'convert temperature' that takes a temperature in celsius as an argument and returns the temperature in fahrenheit
#Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32
a=int(input("enter temperature in celsius:"))
def convert_temperature(a):
    convert_temperature=((a)*(9/5))+32
    return convert_temperature
print(convert_temperature(a))
