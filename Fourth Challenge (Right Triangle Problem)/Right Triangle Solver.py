import math

print("Welcome to the Right Triangle Solver App\n")
firstLeg = float(input("What is the first leg of the triangle: "))
secondLeg = float(input("What is the second leg of the triangle: "))

#calculate third leg with pythagorean theorem c^2 = a^2+b^2
thirdLeg = round(math.sqrt(firstLeg**2 + secondLeg**2),3)

#calculate triangle area 
area = round((1/2)*firstLeg*secondLeg, 3)


#Print the result 
print("\nFor a triangle with legs of "+str(firstLeg)+" and "+str(secondLeg)+" the hypotenuse is "+str(thirdLeg))
print("For a triangle with legs of "+str(firstLeg)+" and "+str(secondLeg)+" the area is "+str(area))

