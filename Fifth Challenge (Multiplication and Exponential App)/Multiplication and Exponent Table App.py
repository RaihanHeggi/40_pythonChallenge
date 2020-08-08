import mpmath as mp
print("Welcome to the Multiplication/Exponent Table App\n")

#getting data 
name = str(input("Hello, what is your name: "))
name = name.title().strip()
number = float(input("What number would you like to work with: "))
message = name + ", Math is cool!"

#calculate multiplication the print 
print('\nMultiplication Table For '+str(number))
for i in range(0,10):
    multiplicationResult = i*number
    print(str(i)+" * "+str(number)+" = "+str(round(multiplicationResult,2)))

#calculate exponential then print
print('\nExponent Table For '+str(number))
for j in range(0,10):
    exponentialResult = mp.power(number,j)
    print(str(number)+" ** "+str(j)+" = "+str(round(exponentialResult,4)))

#print message Math is Cool!
print("\n"+message)
print("\t"+message.lower())
print("\t\t"+message.title())
print("\t\t\t"+message.upper())