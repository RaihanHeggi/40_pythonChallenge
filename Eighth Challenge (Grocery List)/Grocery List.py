import datetime 


#get time 
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

#Welcome message 
print("Welcome to the Grocery List ")
print("Current Time and Date: "+day+"/"+month+" "+hour+":"+minute)
print("You currently have Meat and Cheese in your list")

groceryList = ["Meat","Cheese"]

#inputting value to list 
status = True
while status :
    groceryList.append(str(input("Type of food to add to the grocery list: ")).title())
    check = str(input("inserting again ? (Y/N): "))
    if(check == "N"):
        status = False
    else :
        continue
print("\Here your grocery lust :")
print(str(groceryList))
print("Here is your grocery list sorted :")
groceryList.sort()
print(str(groceryList))

checkStatus = True 
while checkStatus :
    endStatus = str(input("Do you still buying something (Y/N) : "))
    if(len(groceryList) == 0 or endStatus == "N"):
        checkStatus = False
    else :
        print("Currently Item On Grocery List : "+str(len(groceryList)))
        print(groceryList)
        groceryList.remove(str(input("What Food Just You Buy :")).title())
        continue
print("End of Program")