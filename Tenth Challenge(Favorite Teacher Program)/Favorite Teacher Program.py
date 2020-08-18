print("Welcome to Favorite Teacher Program")
fav_teacher = []

for i in range(0,4):
    fav_teacher.append(str(input("Who is your "+str(i+1)+" favorite teacher : ").title()))
print("\nYour favorite teachers ranked is : "+str(fav_teacher))
print("Your favorite teachers alphabetically are: "+str(sorted(fav_teacher)))
print("Your favorite teachers reverse alphabetically are: "+str(sorted(fav_teacher,reverse=True)))

print("\nYour top two teachers are: "+str(fav_teacher[0])+" and "+str(fav_teacher[1]))
print("Your next two teachers are: "+str(fav_teacher[2])+" and "+str(fav_teacher[3]))
print("Your last favorite teacher is : "+str(fav_teacher[len(fav_teacher)-1]))
print("You have "+str(len(fav_teacher))+" favorites teachers.")

#insert
fav_teacher.insert(0,input("\nOops, " + fav_teacher[0] + " is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").title())

print("\nYour favorite teachers ranked is : "+str(fav_teacher))
print("Your favorite teachers alphabetically are: "+str(sorted(fav_teacher)))
print("Your favorite teachers reverse alphabetically are: "+str(sorted(fav_teacher,reverse=True)))


print("\nYour top two teachers are: "+str(fav_teacher[0])+" and "+str(fav_teacher[1]))
print("Your next two teachers are: "+str(fav_teacher[2])+" and "+str(fav_teacher[3]))
print("Your last favorite teacher is : "+str(fav_teacher[len(fav_teacher)-1]))
print("You have "+str(len(fav_teacher))+" favorites teachers.")

#remove 
fav_teacher.remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").title())

print("\nYour favorite teachers ranked is : "+str(fav_teacher))
print("Your favorite teachers alphabetically are: "+str(sorted(fav_teacher)))
print("Your favorite teachers reverse alphabetically are: "+str(sorted(fav_teacher,reverse=True)))

print("\nYour top two teachers are: "+str(fav_teacher[0])+" and "+str(fav_teacher[1]))
print("Your next two teachers are: "+str(fav_teacher[2])+" and "+str(fav_teacher[3]))
print("Your last favorite teacher is : "+str(fav_teacher[len(fav_teacher)-1]))
print("You have "+str(len(fav_teacher))+" favorites teachers.")

