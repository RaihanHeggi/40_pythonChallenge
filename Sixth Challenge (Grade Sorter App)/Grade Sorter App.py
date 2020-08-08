print("Welcome to the Grade Sorter App")

#creating list 
usedList = []

#inputting to the list 
for i in range(0,4):
    usedList.append(int(input("What is your "+str(i+1)+" Grades (0-100) : ")))  

#outputting the list value
print("Your grade are :"+str(usedList))
usedList.sort(reverse=True)
print("\nYour grade from highest to lowest are :"+str(usedList)) 

#removing part 
print("The Lowest two grades will now be dropped.")
status = True
iteration = 0
while status :
    remove = usedList.pop()
    print("Removed grades : "+str(remove))
    if(iteration == 1):
        status = False
    iteration+= 1
print("\nYour remaining grade : "+str(usedList))
print("Nice work! your highest grade is a "+str(usedList[0])+".")
