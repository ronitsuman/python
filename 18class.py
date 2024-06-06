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
# init function automatically callable
class Myclass :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age
    def __str__(self) :
        return f"{self.name} {self.age}"
    def myfunct(self):
        print("Hello"+ " " + self.name   )
    # def myage (self):
    #     print("you are only" + " " + self.age  )

obj = Myclass("john",20)
# print(obj)
obj.myfunct() 
# obj.myage()
obj2 = Myclass("ronit", 22 )
obj2.myfunct()


# Class definition
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing class attributes
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# Accessing instance attributes
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3

print(dog2.name)  # Output: Lucy
print(dog2.age)   # Output: 5

# Calling instance methods
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog2.description())  # Output: Lucy is 5 years old.

print(dog1.speak("Woof Woof"))  # Output: Buddy says Woof Woof
print(dog2.speak("Bark"))       # Output: Lucy says Bark


# inhertance 
# we use parent class every property
class Person:
    def __init__(self,fname,lname) :
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname)

class Student (Person):
    def __init__(self, fname,mname, lname):
        super().__init__(fname, lname)
        self.mname = mname

    def fullname (self):
        print(self.fname,self.mname,self.lname)



rey = Student("ronit","suman","deo")
rey.fullname()
rey.printname()





