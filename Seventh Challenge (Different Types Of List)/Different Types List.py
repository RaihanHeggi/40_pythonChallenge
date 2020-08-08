#declaring 4 different list 
num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

#print table 
print("\n\t\tSummaty Table ")

print("\nThe Variable num_strings is a "+str(type(num_strings)))
print("it contains the elements: "+str(num_strings))
print("First element is a "+str(type(num_strings[0])))

print("\nThe Variable num_ints is a "+str(type(num_ints)))
print("it contains the elements: "+str(num_ints))
print("First element is a "+str(type(num_ints[0])))

print("\nThe Variable num_floats is a "+str(type(num_floats)))
print("it contains the elements: "+str(num_floats))
print("First element is a "+str(type(num_floats[0])))

print("\nThe Variable num_lists is a "+str(type(num_lists)))
print("it contains the elements: "+str(num_lists))
print("First element is a "+str(type(num_lists[0])))

#sorting list string and ints 
num_strings.sort()
num_ints.sort()

print("\nNow sorting num_strings and num_ints ")
print("Sorted num_strings "+str(num_strings))
print("Sortes num_ints "+str(num_ints))
print("\nStrings are sorted alphabetically while integers are sorted numerically!!!")