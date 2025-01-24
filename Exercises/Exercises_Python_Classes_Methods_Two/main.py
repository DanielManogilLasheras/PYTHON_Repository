import datetime
class Pet():
    """A class to capture useful information regardin my pets, in case I lose them"""

    def __init__(self, height):
        self.height = height

    is_human = False
    owner = "smith"

    @classmethod
    def owned_by_smith(cls):
        return 'Smith' in cls.owner

    @classmethod
    def create_random_height(cls):
        import random
        height = random.randrange(0, 100)
        return cls(height)

    def __str__(self):
        # %s are the variables to be filled. % is the conversion from the statement to the variables, then we put the variables
        return '%s (height : %s cm) ' % (self.name, self.height)

    def is_tall(self, tall_if_at_least):
        return self.height >= tall_if_at_least

    @staticmethod
    def owned_by_smith_family():
        return 'smith' in Pet.owner

#exercise 14 line 46
for i in range(5):
    pet = Pet.create_random_height()
    print (pet.height)


##Execise 15
class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

freezing = Temperature(100)

my_temp = Temperature(100)
print (my_temp.fahrenheit)

my_temp_two = Temperature(0)
print (my_temp_two.fahrenheit)

#Exercise 16
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(self):
        print('Hello, my name is %s' % self.first_name)
    @property
    def full_name(self):
        return '%s %s' % (self.first_name,self.last_name)
    @full_name.setter
    def full_name(self,name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last
customer = Person ('Alvaro', 'Rodriguez')
print(customer.full_name)

customer.full_name = 'Mary Lou'
print (customer.full_name)

#Exercise 17
class Pet:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class Cat(Pet):
    is_feline = True
class Dog(Pet):
    is_feline = False
my_cat = Cat('Kibbles','8')

#Exercise 18
class Baby(Person):
    def speak (self):
        print ('BLABLABABABABABAB')

class Adult(Person):
    def speak(self):
        print('Hello, my name is %s' % self.first_name)

jess = Baby('Jessie', 'Mcdonald')
tom = Adult('Thomas', 'Smith')
print(jess.speak())
print(tom.speak())

#Exercise 19
class MyInt(int):
    def is_divisible_by(self, x):
        return self % x == 0

#Exercise 20

import datetime
class MyDate(datetime.date):
    def add_days(self, n):
        return self + datetime.timedelta(n)
d = MyDate(2019, 12, 1)
print(d.add_days(40))
print(d.add_days(400))

#Exercise 21
class BetterPerson(Person):
    @property
    def full_name(self):
        return '%s %s' % (self.first_name,self.last_name)
    @full_name.setter
    def full_name(self, name):
        names = name.split(' ')
        self.first_name = names[0]
        if len(names) > 2:
            self.last_name = ' ' .join(names[1:])
        elif len (names) == 2:
            self.last_name = names[1]

my_person = BetterPerson('Mary', 'Smith')
my_person.full_name = 'Mary Anne Smith'
print(my_person.first_name)
print(my_person.last_name)

#Exercise 22
class TalkativePerson(Person):
    def speak(self):
        super().speak()
        print('It is a pleasure to meet you')
john = TalkativePerson('John', 'Tomic')
john.speak()

#Exercise 23
class Diary():
    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas
    @staticmethod
    def format_date(date):
        return date.strftime('%d-%b-%y')
    def show_birthday(self):
        return self.format_date(self.birthday)
    def show_christmas(self):
        return self.format_date(self.christmas)

class CustomDiary(Diary):
    def __init__(self, birthday, christmas, date_format):
        self.date_format = date_format
        super().__init__(birthday, christmas)

first_diary = CustomDiary(datetime.date(2018,1,1), datetime.date(2018,3,3), '%d-%b-%Y')
second_diary = CustomDiary(datetime.date(2018,1,1), datetime.date(2018,3,3),'%d/%m/%Y')
print(first_diary.show_birthday())
print(second_diary.show_christmas())


#Exercise 23, using Person, Baby and Adult classes
class Calendar():
    def book_appointment(self,date):
        print ('Booking appointment for date %s' % date)

class OrganizedAdult(Adult, Calendar):
    pass
class OrganizedBaby(Baby, Calendar):
    def book_appointment(self,date):
        print('Note that you are booking an appointment with a baby')
        super().book_appointment(date)

andres = OrganizedAdult('Andres', 'Gomez')
boris = OrganizedBaby('Boris', 'Bumblebutton')
andres.speak()
boris.speak()
boris.book_appointment(datetime.date(2018,1,1))


#Exercise 24
import math
class Polygon:
    def __init__(self,num_of_sides):
        self.num_of_sides = num_of_sides

    def give_sides(self):
        return self.num_of_sides
    @property
    def perimeter(self, radius):
        return radius * math.pi ** 2
    def __str__(self):
        return 'Polygon with %s sides' % self.num_of_sides

class Rectangle(Polygon):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        super().__init__(num_of_sides = 4)
        
    @property
    def area(self):
        result = self.base * self.height
        return 'The area of %s * %s is %s' % (self.base, self.height, result)

rectangle = Rectangle(5,2)
print (rectangle.area)
