print("Welcome to Letter Counter Program")
name = str(input("\nWhat is Your Name: "))
print("Hello, "+name.title().strip()+"!")
print("I will count the number of times that a specific letter occurs in a message")
message = str(input('\nPlease enter a message: '))
inputCheck = str(input("\nWhich letter would you like to count the occurrences of: "))

#standarize methods
messageStandart = message.lower()
inputStandart = inputCheck.lower()

countingResult = messageStandart.count(inputStandart)
print("\n"+name.title().strip()+", your message has "+str(countingResult)+" "+inputCheck.upper()+" and "+inputStandart+"'s in it.")