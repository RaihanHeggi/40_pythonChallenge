print("Welcome to the MPH and MPS Conversion App\n")

#getting MPH value
milesPerHour = float(input('What is your speed in miles per hour: '))

#conversion MPH to MPS and Print it
conversionToMPS = milesPerHour * 0.4474
print("Your speed in meter per second is "+str(round(conversionToMPS, 2)))
