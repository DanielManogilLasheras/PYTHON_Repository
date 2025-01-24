import math

#Exerc One

x = 10
print(x)

print(type (x))
print (x.bit_length())

print (x.__doc__)

#Exerc Two

my_string = 'hello World!'
print (type(my_string))
print (my_string.__doc__)

print (my_string.__dir__())

print(my_string.capitalize())   
print(my_string.upper())
print(my_string.replace(" ", "_"))

#Exercise Three

class Australian():
    is_human = True
    enjoys_sport = True

    @classmethod
    def is_sporty_human(cls):
        return cls.is_human and cls.enjoys_sport
john = Australian()

print (type(john))

print (john.is_human)
print (john.enjoys_sport)

ming = Australian()



#Exercise 9
class Pet():
    """A class to capture useful information regardin my pets, in case I lose them"""
    #Exercise Four
    
    def __init__(self,name,height):
        self.name = name
        self.height = height
    is_human = False
    owner = "smith"
    @classmethod
    def owned_by_smith(cls):
        return 'Smith' in cls.owner
    @classmethod
    def create_random_height(cls):
        import random
        height = random.randrange (0, 100)
        return cls(height)
    def __str__(self):
        #%s are the variables to be filled. % is the conversion from the statement to the variables, then we put the variables 
        return '%s (height : %s cm) '% (self.name,self.height)
    def is_tall(self,tall_if_at_least):
        return self.height >= tall_if_at_least

    @staticmethod
    def owned_by_smith_family():
        return 'smith' in Pet.owner
    

chubbles = Pet(name = 'Chubbles',height = 5)
print(chubbles.is_human)
print(chubbles.owner)
print(chubbles.__doc__)

print(chubbles.height)


#Exercise Five
class Circle():
    is_shape = True
    def __init__(self,radius,color="red"):
        self.radius = radius
        self.color = color

    def area(self):
        return math.pi * self.radius ** 2

first_cicle = Circle (5,"red")
second_circle = Circle(10,"blue")

print (first_cicle.radius)
print (second_circle.color)

third_circle = Circle(12)
print (third_circle.color)


#Exercise Six
#Exercise Eight
##SELF REPRESENTS THE INSTANCE(THTA IS THE OBJECT) WITHIN THE METHOD
class Country():
    def __init__(self,name='unspecified' , population=None , size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq
    @classmethod
    def create_with_msq(cls, name, population, size_msq):
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, population, size_kmsq)
    def size_miles_sq(self,conversion_rate = 0.621371):
        return self.size_kmsq * conversion_rate ** 2

    def __str__(self):
        label = self.name
        if self.population:
            label = '%s, population: %s' % (label, self.population)
        if self.size_kmsq:
            label = '%s, size_kmsq: %s' % (label, self.size_kmsq)
        return label

    
usa = Country(name = 'United States of America' , size_kmsq=9.8e6)


print(usa.__dict__)


#Exercise Seven creating method of instanced object
bowser = Pet('Bowser',60)

print (bowser.is_tall(80))

algeria = Country(name='Algeria',size_kmsq=2.382e6)
print (algeria.size_miles_sq())
print (algeria.size_miles_sq(conversion_rate=0.6))

print(chubbles)

print (usa)

#Exercise 10
nibbles = Pet("nibbles",100)
print(nibbles.owned_by_smith_family())

#Exercise 11
import datetime
class Diary():
    def __init__(self,birthday,christmas):
        self.birthday = birthday
        self.christmas = christmas
    @staticmethod
    def format_date(date):
         return date.strftime('%d-%b-%y')
    def show_birthday(self):
        return self.format_date(self.birthday)
    def show_christmas(self):
        return self.format_date(self.birthday)


diary = Diary(datetime.date(2020, 5, 1), datetime.date(2020, 12, 25))

print (diary.show_birthday())
print (diary.show_christmas())

#Exercise 12 line  31

aussie = Australian()
print(aussie.is_sporty_human())

#Exercise 13 line 96
mexico = Country.create_with_msq('Mexico', 150e6, 760000)
print(mexico.size_kmsq)

