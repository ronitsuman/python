# classes = blueprint
# class name start with capital

# class Myclass :
#     x = 5 


# obj = Myclass()
# print(obj.x)


# class Myclass :
#     def __init__(self,name,age) :
#         self.name= name 
#         self.age = age


# obj = Myclass("john",20)
# print(obj.name)

# class Myclass :
#     def __init__(self,name,age) :
#         self.name= name 
#         self.age = age


# obj = Myclass("john",20)
# print(obj.age)

# class Myclass :
#     def __init__(self,name,age) :
#         self.name= name 
#         self.age = age
#     def __str__(self) :
#         return f"{self.name} {self.age}"

# obj = Myclass("john",20)
# print(obj)

# ek bluprint hai object jo hota diffrent ho skta hai 
# class name should always be in capital 
class Myclass :
    def __init__(self,name,age) :
        self.name= name 
        self.age = age
    def __str__(self) :
        return f"{self.name} {self.age}"
    def myfunct(self):
        print("Hello"+ " " + self.name )
    def myage (self):
        print("you are only" + " " + self.age  )
obj = Myclass("john",20)
# print(obj)
obj.myfunct() 
obj2 = Myclass("ronit", 22 )
obj2.myfunct()
obj2.myage()

