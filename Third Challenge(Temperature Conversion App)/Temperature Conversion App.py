print("Welcome to the Temperature Conversion Program\n")
#getting Fahrenheit Temperature
fahrenheitTemp = float(input("What is the given temperature in degrees Fahrenheit: "))

#convert to another Temperature system
celciusTemp = (5/9)*(fahrenheitTemp-32)
kelvinTemp = celciusTemp + 273.15

#Print all Result
print("\nDegrees Fahrenheit: "+str(round(fahrenheitTemp,4)))
print("Degrees Celcius: "+str(round(celciusTemp,4)))
print("Degrees Kelvin: "+str(round(kelvinTemp,4)))