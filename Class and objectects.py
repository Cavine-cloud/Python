#class is a blueprint for creating objects,it defines a set of attributes and methods that the created object will have

#Template 
# class ClassName:#class declaration
#     #class attributes
#     class_atrribute='value'

#     def Method_name():
#         #method block



# class Dog:
#     species='canis lupus'
#     def __init__(self,name,age):
#         print("the constractor is called")
#         self.name=name #instance attribute
#         self.age=age #instance attribute

#     def bark(self): #self is a special parameter in a class method that refers to the instance of the class itself
#         print("the class method is called")
#         return f"says woof!"
    
# #object- an object is an instance of a class (my_dog)
# my_dog=Dog("Buddy",5)
# print(my_dog.age) #acces instance attribute age
# print(my_dog.name) #acces instance attribute name


#dry
# code reusability

# class Car:
#     #constractor
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.speed=0

#     #method
#     def accelerate(self,speed):
#         self.speed+=speed
#         return f"The {self.make} {self.model} has accelerated to {self.speed} "
    
#     #method
#     def brake(self,decelerate):
#         self.speed-=decelerate
#         return f"the {self.make} slowed down to {self.speed}"
    
#     #method
#     def displaySpeed(self):
#         return f"the speed is {self.speed}"
    
# my_car=Car("Toyota","Camry",2024)
# print(my_car.displaySpeed())#speed is at 0
# print(my_car.accelerate(5)) #accelerate by 5
# print(my_car.displaySpeed()) #new speed of 5
# print(my_car.accelerate(15)) #increment speed by 15
# print(my_car.displaySpeed())
# print(my_car.brake(10))
# print(my_car.displaySpeed())

# my_car2=Car("mercedes","c200",2015)
# print(my_car2.displaySpeed())
# print(my_car2.accelerate(10))
# print(my_car2.displaySpeed())


class Book:
    #constructor
    def __init__(self,title,page):
        self.title=title
        self.page=page

    def showBookDetail(self):
        return f"your book title is {self.title} with {self.page} pages"


my_book_1=Book("blossoms of the savanna",900)#object declaration
my_book_2=Book("1984",900)#object declaration
my_book_3=Book("The midnight library",1000)#object declaration
my_book_4=Book("kigogo",600)#object declaration
my_book_5=Book("circle",1200)#object declaration



print(my_book_1.showBookDetail())#method call for my_book_1 object
print(my_book_5.showBookDetail())
# #inheritance
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def ShowPersonDetail(self):
#         return f"Hello my name is {self.name} and i am {self.age} years old"


# class Child(Person):#we want to inherit attributes of the Person class
#     def __init__(self,childName,childAge,childsParent):
#         #we call the parent class constractor to inherit the Person attribute
#         super().__init__(childsParent.name,childAge)
#         self.childName=childName
#         self.childsParent=childsParent
#     def showChildDetail(self):
#         return f"hello, i am {self.childName},and my parent is {self.name}"


# parent=Person("john",40)#parent object
# child=Child("joseph",10,parent)#child object is inheriting the parents attributes 

# print(child.showChildDetail())

class Animal: #parent class animal
    def speak(self):
        print("animal is speaking")

class Dog(Animal): #child class Dog {inheriting the attributes of speak from the parent class}
    def speak(self):
        super().speak()#executes the speak method from the parent
        print("Woof!,Woof!") 

my_dog=Dog()#object from the child
my_dog.speak()


# why use Super?
# 1. you can call the parent method and constractor without duplicating code thus maintaining {D.R.Y} and clean code
#inheritance we in heriting the attributes



#parent class 
class Vehicle:
    def __init__(self,brand): #brand as attribute/argument
        self.brand=brand
    def move(self):
        print(f"{self.brand} is moving")

#child 
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def honk(self):
        print(f"{self.brand},{self.model} is honking")
    
# Creating an object of the Car class, passing brand and model
car = Car("Toyota", "Camry")  # Pass the brand and model separately

car.honk()

            ############EXAMPLE###########

class Parent:
    def __init__(self,FathersName,FathersAge,MothersName,MothersAge):
        self.FathersName=FathersName #attribute of fathers name in the Father class
        self.FathersAge=FathersAge
        self.MothersName=MothersName
        self.MothersAge=MothersAge
    def showParentDetails(self):
        return f"The parents are {self.FathersName} and {self.MothersName}"

class Child(Parent):
    def __init__(self,ChildName,ChildAge,FathersName,FathersAge,MothersName,MothersAge):
        super().__init__(FathersName,FathersAge=FathersAge,MothersName=MothersName,MothersAge=MothersAge)
        self.ChildName=ChildName
        self.ChildAge=ChildAge
    def ShowChildDetails(self):
        print(f"the Child's Name is {self.ChildName} and the childs age is {self.ChildAge} and the parents are {self.FathersName},{self.MothersName}")


theParent=Parent("Joseph",45,"Mary",43) #Object extending the Parent class

theSecondParents=Parent("Joshua",33,"Eliza",30) #Object extending the Parent class


child1=Child("Mark",12,theParent.FathersName,theParent.FathersAge,theParent.MothersName,theParent.MothersAge) #has inherited theparent attributes
child2=Child("Eva",10,theParent.FathersName,theParent.FathersAge,theParent.MothersName,theParent.MothersAge) #has inherited theparent attributes
child1.ShowChildDetails() #we are calling child 1 showdetail method that is inheriting theparent
child2.ShowChildDetails() #we are calling child 1 showdetail method that is inheriting theparent


child3=Child("Natalie",2,theSecondParents.FathersName,theSecondParents.FathersAge,theSecondParents.MothersName,theSecondParents.MothersAge)
child3.ShowChildDetails()# the object is inheriting thesecondparents Objects

