thisdict = {
    "fname":"ronit",
    "lname": "suman",
    "age":20
}
# print(thisdict["age"])
# print(len(thisdict))

child1 = {"fname":"ronit", "lname" : "suman","year" :2005}
child2 = {"fname":"sumit", "lname" : "kumAR","year" :2004}
myfamily = { "child1":child1,"child2":child2}
# print(myfamily["child2"]["year"])

mynewfamily  = myfamily
# print(mynewfamily)
child1.popitem()
print(child1)
print(child1.values())


dictt = {"name" : "ronit", 
         "age " : "24" , 
         "gender ": "male" }


print(dictt.values())

