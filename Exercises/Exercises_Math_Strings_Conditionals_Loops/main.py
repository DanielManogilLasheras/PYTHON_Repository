#Exercise One
from itertools import filterfalse
from xml.etree.ElementTree import tostring

print(type(6))
print (type(6.0))
print (float(6))
#Exercise Two
x = 14
x += 1
x = (x /5) ** 2
print (x)
#Exercise Three
print((2 + 3j) / (1 - 5j))
#Exercise Four
first_number=1
x = 5
y = 2
print(x + x - y ** 2)
#Exercise Five
x , y = 8 ,5
print(x // y)
#Exercise Six
#This is a comment

##Exercise Seven: Pythagorean Theorem
x , y , z = 2 , 3 , 4
result = x ** 2 + y ** 2 + z ** 2
result = result ** 0.5
print(result)

##Exercise Eight
bookstore = 'City Lights'
bookstore = 'Moe\'s'
vacation_note = '''
During our vacation to San Francisco, we waited in a long line by
Powell St. Station to take the cable car. Tap dancers performed on
wooden boards. By the time our cable car arrived, we started looking
online for a good place to eat. We're heading to North Beach.
'''

greeting = 'Hello'
print(greeting * 5)

#Exercise Nine
italian_salute = 'Ciao'
print ('Should we greet with' , italian_salute , 'in North Beach?')

owner = 'Lawrence'
age = 100
print ('The founder of the city is named {} , and is now  {}  old'.format(owner,age))

name = 'corey'
print(name.capitalize())
print(name.upper())
print(name.count('o'))

x = '5'
x=int(x)
y = 5 + x
print(y)

print('What is your name')
name = 'world' #input()
print ('Hello' , name)

#Exercise Ten
destination = 'San Francisco'
print(destination[0])
print(destination[-1])
print(destination[-2])
print(destination[4:10]) # The upper bound is never included
print(destination[:8])
print(destination[-3:])
print(destination[:4])
print(len(destination))

#Exercise Eleven
over_18 = True
print(over_18)

over_21 = False
print(type(over_21))

print (over_18 or over_21)
print(over_18 and over_21)
print (not over_18)
print (not over_21 or(over_21 or over_18))

#Exercise Twelve
print('Enter a number to see if it\' a perfect square')
#number = input()
number = 9
number = abs(int(number))
i = -1
square = False
while i <= number**(0.5):
    i+=1
    if i*i == number:
        print ('the square root of' , number , 'is' , i , '.')
    else:
        print('', number, 'is not a perfect square')

#Exercise Thirteen
print('A one bedroom in the Bay Area listed at $599.000')
print('Enter your first offer on the house')
offer = 500000
#offer = abs(int(input()))
print('Enter your best offer on the house')
#best = abs(int(input()))
best = 690000
print('How much do you want to offer each time?')
#increment = abs(int(input()))
increment = 50000
offer_accepted = False
while offer <= best:
    if offer >= 650000:
        offer_accepted = True
        print ('Your offer of' , offer , 'has been accepted')
        break
    else:
        print('We\'re sorry, your offer of' , offer , 'has not been accepted')
        offer += increment

#Exercise Fourteen
for i in 'Portland':
    print (i)

#Exercise fifteen
for i in range(1,10):
    print(i)

for i in range(10): print(i)
for i in range (0 , 10 , 2):
    print(i)
for i in range (3 , 0 , -1):
    print(i)
name = 'Dani'
for i in range (3):
    for j in name:
        print(j)

#Exercise Sixteen
for num in range(10 , 100):
    if num % 2 == 0:
        continue
    if num % 3 == 0:
        continue
    print(num)

#Exercise seventeen
print('Hi, I\'m the first conversational bot')
print('What is your name?')
##answerTwo = input()
answerTwo = 'Daniel'
print('Do you like tomatoes' , answerTwo , '?')
#answer = input()
answer = 'Yes'
check = False
while not check:
    if answer.lower() == 'yes':
        print('Very nice' , answerTwo , 'I like tomatoes too')
        check = True
    elif answer.lower() =='no':
        print('Not everybody can have g'
              'ood taste')
        check = True
    else:
        print('I did not understand the answer, repeat')
        answer=input()

print('Hi, I\'m the second conversational bot')
print('On a scale of 1 to 10, how smart do you think you are')
answer = input()
check = False
while not check:
    check = True
    if type(answer) !=  type(int) or int(answer) <=0 or int(answer) >=11:
        print('That\'s not a valid number, try again')
        answer = input()
        check = False
    elif int(answer) in range (1,3):
        print('I guess you are not very smart')
    elif int(answer) in range(4,6):
        print('So you are average')
    elif int(answer) in range(7,10):
        print('Wow you are so smart')
