'''
Created on Jul 9, 2014

@author: viejoemer

HowTo add and remove element into a set?

¿Cómo añadir y quitar elementos en un conjunto?

add(elem)
Add element elem to the set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not
contained in the set.
'''

#Create a set with values.
s_1 = set()
print("set one", s_1)

#Adding element into a set
s_1.add(1)
print("set with one element add", s_1)

#Remove a element from a set
s_1.remove(1)
print("set with one element remove", s_1)

#If you try to remove a element Raises KeyError if elem is not
#contained in the set.
s_1.remove(1)
print("set with one element remove", s_1)