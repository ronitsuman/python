# myset = {"apple","orange" , "gauva","amrood"}
# myset2 = set(("aam","imli","kathmitthi"))



# print(type(myset))
# print(myset2)

# in set we cannot add same number aur string in it they only show single
# duplicity is not allowed

thisset = {1,2,2,3,4,4,5}
thisset.add(7) #add element in set
thisset2 = {1,2,3,4,5,5,5,1,1,True,False} #false is indicate as 0
thisset.update(thisset2) #add items in a set and list and any string we can add
thisset.remove(1) # Remove items in a set
thisset3 = thisset.intersection(thisset2)

print(thisset)
print(thisset2)
print(type(thisset))
print(thisset3)
