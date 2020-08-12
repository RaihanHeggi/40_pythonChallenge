print("Welcome to the Basketball Roster Program\n")

basketBall = []
for i in range(0,5):
    if (i == 0):
        basketBall.append(str(input("Who is yout point guard: ")).title())
    elif(i == 1) :
        basketBall.append(str(input("Who is yout shooting guard: ")).title())
    elif(i == 2):
        basketBall.append(str(input("Who is yout small forward: ")).title())
    elif(i == 3):
        basketBall.append(str(input("Who is yout power forward: ")).title())
    else :
        basketBall.append(str(input("Who is yout center: ")).title())
    
print("\n\t\tYour Starting 5 for the upcoming basketball season")
for j in range(len(basketBall)):
    if (j == 0):
        print("Point Guard:\t\t"+basketBall[j])
    elif(j == 1) :
        print("Shooting Guard:\t\t"+basketBall[j])
    elif(j == 2):
        print("Small Forward:\t\t"+basketBall[j])
    elif(j == 3):
        print("Power Forward:\t\t"+basketBall[j])
    else :
        print("Center:\t\t\t"+basketBall[j])
print("\nOh no, "+basketBall[2]+" is injured.")
characterInjured = basketBall[2]
basketBall.pop(2)
print("Your roster only has "+str(len(basketBall))+" players.")
basketBall.insert(2,str(input("Who will take "+characterInjured+"'s spot: ")))
for k in range(len(basketBall)):
    if (k == 0):
        print("Point Guard:\t\t"+basketBall[k])
    elif(k == 1) :
        print("Shooting Guard:\t\t"+basketBall[k])
    elif(k == 2):
        print("Small Forward:\t\t"+basketBall[k])
    elif(k == 3):
        print("Power Forward:\t\t"+basketBall[k])
    else :
        print("Center:\t\t\t"+basketBall[k])
print("\nGood Luck "+basketBall[2]+" you will do great")
print("Ypur roster only has "+str(len(basketBall))+" players.")