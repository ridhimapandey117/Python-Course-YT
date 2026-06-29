#/////////////////////////////////////
#OBJECT ORIENTED PROGRAMMING
#/////////////////////////////////////

#This is how class headers are constructed
class Dog():

    #Class object attribute, same for any instance of a class, kinda like a static variable
    species = 'mammal'

    def __init__(self, breed, name):  #called when u need to make an instance of a class
        self.breed = breed
        self.name = name

    #Operations/Actions --> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

my_dog = Dog(breed='Lab', name='Stacy')
my_dog.bark(5)


class Circle():

    #Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*Circle.pi

    #Methods

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
print(my_circle.get_circumference())
print(my_circle.area)

#/////////////////////////////////////
#INHERITANCE/POLYMORPHISM
#/////////////////////////////////////

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

my_animal = Animal()
my_animal.eat()

class Dog(Animal):  #adding animal in the parenthesis is like adding extends parent class

    def __init__(self):
        Animal.__init__(self) #This is like doing super(n1,n2)
        print("Dog Created")

    def who_am_i(self): #polymorphism is basically when the same method exists in the parent and child classes, when the method is called, the child class' version will be used instead
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF")

my_dog = Dog()
my_dog.who_am_i() #Dog will inherit classes of Animal

#/////////////////////////////////////
#Special Methods
#/////////////////////////////////////

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): #python equivalent of a toString
        return f"{self.title} by {self.author}"

    def __len__(self): #returns len of object
        return self.pages

    def __del__(self): #Will display message when I call del [object]
        print("A book object has been deleted")

b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b #deletes an object from memory

#/////////////////////////////////////
#OOP HOMEWORK
#//////////////////////////////////////

#Problem 1
class Line:

    def __init__(self,coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return (((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1]-self.coor1[1])**2)) ** 0.5

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())

#Problem 2
class Cylinder:

    def __init__(self, height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius * self.radius * self.height

    def surface_area(self):
        return (2*3.14*self.radius*(self.radius + self.height))

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())

#Challenge
class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("Deposit Accepted")

    def withdraw(self, money):
        if (money > self.balance):
            print("Funds Unavailable!")
        else:
            self.balance -= money
            print("Withdrawal Accepted")

    def __str__(self):
        return f"Account owner:\t{self.owner}\nAccount balance:\t${self.balance}"

acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(500)

