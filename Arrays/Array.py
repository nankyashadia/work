import array
import numpy as np
# An array is a special variable that can hold more than one value at a time
#An array of colors
colors=['blue',"yellow","black","purple","aqua","marron","blue-black"]
print (colors)
#accessing the elements in that array
b=colors[6]
c=colors[2]
print(c)
print (b)
#modifying elements in the array

colors[3]="orange"
print (colors)
#length of the array
a=len(colors)
print(a)
#looping array elements we use for in
for y in colors:
    print(y)
    
    #adding elements in array
colors.append("green")
colors.append("brown")
colors.append("brown")
print(colors)
#removing elements from the array
colors.pop(0)
print(colors)
#using the remove method
colors.remove("brown")
print (colors)
#copy method , it copies the elements in the array
w=colors.copy()
print(w)
# clear() it clears the list
#colors.clear()
#print(colors)
z=colors.count("brown")
print(z)
    #extend() it adds the The extend() method adds the specified list elements (or any iterable) to the end of the current list
Animals=["cow","cat","goat"]
colors.extend(Animals) 
Animals.extend(colors)
print(colors)
#print(Animals) 
# index() shows the position of the element in the array
g=colors.index("aqua")
print(g)
#colors.insert(5,67)
colors.insert(8,"red")
print(colors)
print(colors)
# reverse() it reverses the elements of the array
colors.reverse()
print (colors)
#sort() it sorts the list alphabetically
colors.sort()
print(colors)
#sorting in descending order
colors.sort(reverse=True)
print(colors)
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
colors.sort(key=myFunc)

print(colors)

