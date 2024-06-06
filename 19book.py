# first we have to create a class (always uppercase)

class Dog :
    # then the init is required to taking the outut
    def __init__(self,name,age) :
        self.name = name
        self.age = age 
        # then second we have to create a function if i call bark then response should be change

    def bark(self):
        print("bhoow bhoow!")
        # then we have to create a method like dogdetail,age
    def dogdetail(self):
        print("my dog name is "+ self.name +" "+ "her age is " + " " + str(self.age))
    def Age (self):
        print("dog age is "+ str(self.age))

# then create a object we can use in 
dog = Dog("fido", 3)
# then according to output we can call them 
print(dog.name)

print(dog.age)
dog.bark()
dog.dogdetail()
dog.Age()

class Car :
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year 
    def car_info(self):
        return f"{self.year},{self.make},{self.model}"
    
    def age(self):
        current_year = 2024
        return current_year - self.year

car = Car("toyata","coroola",2019)
print(car.car_info())

car.car_info()
print(car.age())

# create a function follow the process
# def function-name(parameter):
def greet (name):
    print("hello" + " " + name + " ! ")


# then we have to simply call the function 
greet("ronit")

# lets create another function of telling her age 
def age (age):
    print("I am " + " " + str(age) + " year old")  

age(20)  

def selfinformation(name,age ):
    print("My Name is " + " " + name + "."  )
    print("I am " + " " + str(age) + " year old . ")
    
selfinformation("Ronit",24)


class Cat :
    def __init__(self,name,breed,age,color) :
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
    def bark (self):
        print("bhaow bhaow ! ")
    def wagtail(self):
        print("waagging tail ....")
    def catinfo (self):
        print("my cat name is" + " " + self.name)
        print("my cat breed is" + " " + self.breed)
        print("my cat age is" + " " +str(self.age))
        print("my cat color is" + " " + self.color)

cat = Cat("meow","angreji",23 , "black")

print(cat.catinfo())

selfinformation("Ronit suman" , 25)

# interface vs abstract class 
# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass

# Shape()
        
class Square ():
    def __init__(self,side_length ):
        self.side_length = side_length
    def get_area(self):
        return self.side_length ** 2
    def get_perimeter(self):
        return self.side_length * 4
    
my_square = Square(10)
print(my_square.get_area())
print(my_square.get_perimeter())


# 



    

    

    