#Exercise One
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
print(len(destination))
