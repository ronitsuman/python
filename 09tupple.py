# mytuple = ("apple", "banana","cherry")
# mylist = list(mytuple)
# mylist.append("orange")
# mynewtuple = tuple(("red", "black"))

# print(mytuple)
# print(type(mytuple))
# print(mylist)
# print(type(mylist))
# print(mynewtuple)
# print(type(mynewtuple))
# print(len(mynewtuple))

# tupple if condition

# mytuple = ("apple", "banana","cherry")
# # print(mytuple[0:2])
# if "apple" in mytuple :
#     print("yes apple is in list")

# tupple to list 
# list to tupple 
# append matlab daalna naya item 

# mytuple = ("apple", "banana","cherry")
# myList = list(mytuple)
# myList.append("onion")
# myList[1] = "gauva"
# mytuple = tuple(myList)

# print(mytuple,myList)

# packing tuple

# mytuple = ("apple", "banana","cherry")
# y = ("orange",)
# mytuple += y
# print(mytuple)



# unpacking tuple 
# and creating in a variable

mytuple = ("apple", "banana","cherry" , "Hello","World" , "i am ronit")
# (a,b,c,*d,e) = mytuple
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

multituple = mytuple*2

print(multituple)
