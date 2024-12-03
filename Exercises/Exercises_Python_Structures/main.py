#Exercise One, this is a list, it has it's own distinct position and index
shopping = ["bread","milk","eggs"]
print(shopping)

for item in shopping:
    print(item)

mixed = [365,"days",True]
print(mixed)

#Exercise Two
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
print('...')
for row in matrix:
    for col in row:
        print(col)

#Exercise Three
matrix = [['John Mckee',38,'Sales'],['Lista Crawford',29,'Marketing'],['Sujan Patel',33,'HR']]
for row in matrix:
    print(row)
    print('Name:' , row[0])
    print('Age:' , row[1])
    print('Department:', row[2])
    print('--------------')

#Exercise Four
x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10,11,12],[13,14,15],[16,17,18]]
z = [[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(z)):
    for column in range(len(z)):
        z[row][column]=x[row][column]+y[row][column]
print(z)

for row in range(len(z)):
    for column in range(len(z)):
        z[row][column]=x[row][column]*y[row][column]
print(z)
print('--------------')

#Exercise Five
shopping=["bread","milk","eggs"]
print(len(shopping))
list1 = [1,2,3]
list2 = [1,2,3]
final_list = list1 + list2
print (final_list)

list3 = ['oi']
print(list3 *  3)

#Exercise Six
shopping.append("potatoe")
print(shopping)
shopping.insert(2,"oranges")
print(shopping)

#Exercise Seven
employee = {
    'name' : "Jack Jackson",
    'age' : "30",
    'department' : "sales"
}

movie = {
    'title' : "The godfather",
    'director' : "Francis Ford Coppola",
    'year' : 1972,
    'rating' : 9.2
}
print(movie['year'])
movie['rating'] = (movie['rating'] + 9.3)/2
print(movie['rating'])

movie['actors'] = ['Marlon Brando', 'Al Pacino' , 'James Caan']
movie['other_details'] = {
    'runtime': 175,
    'language': 'English'
}
print(movie)

employees=[]
employee1 = {
    'name': "John Mckee",
    'age': 38,
    'department': "sales"
}
employees.append(employee1)
employee2= {
    'name':"Lisa Crawford",
    'age':29,
    'department':"Marketing"
}
employees.append(employee2)
employee3= {
    'name':"Sujan Patel",
    'age':33,
    'department':"HR"
}
employees.append(employee3)
print(employees[-1])

#Exercise Eight
items = ['apple', 'orange', 'banana']
quantity = [5,3,2]

orders = zip(items,quantity)
#Each time we need to call the zip again as it's a full iterator and won't let us convert it
#print(tuple(orders))
#print(list(orders))
print(dict(orders))

#Exercise Nine
orders = {'apple':5, 'orange':3, 'banana':2}
print(orders.values())
print(list(orders.values()))

print(list(orders.keys()))
for tuple in list(orders.items()):
    print(tuple)

#weekdays_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_tuple=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


#Exercise Ten
t = ('bread','milk','eggs')
print(len(t))
print (t + ('apple', 'orange'))

t_mixed = 'apple' , True ,  3
print(t_mixed)
t_shopping = ('apple',3), ('orange',2),('banana',5)
print(t_shopping)

#Una lista es un conjunto desordenado de elementos que puede variar en su forma u orden
#Un diccionario es una lista que establece un objeto con pares de key-value
#Una tupla es una lista inmutable, y sus nombres no pueden ser cambiados tras inicializarse, se pueden usar para representar colecciones fijas de items
#Un set es una coleccion desordenada de objetos inmutables que soportan operaciones mimicking la teoria del set matemático.
#Un set no permite multiples ocurrencias del mismo elemento, y pueden ser usados para efectivamente prevenir valores duplicados.


#Exercise Eleven
s1 = set([1,2,3,4,5,6])
print(s1)
s2 = set([1,2,2,3,4,4,5,6,6])
print(s2)
s3 = set([3,4,5,6,6,6,1,1,2])
print(s3)
#El set ordena automáticamente los valores siguiendo su logica

s4={"apple","banana","orange"}
print(s4)
s5={'apple','banana','orange'}

s4.add('pineapple')
print(s4)

#Exercise Twelve
s5 = {1,2,3,4}
s6 = {3,4,5,6}
print (s5 | s6)
print(s5.union(s6))

print (s5 & s6)
print (s5.intersection(s6))

print(s5 - s6)
print (s5.difference(s6))

print (s5 <= s6)
print(s5.issubset(s6))
s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))
print('.')
print(s7<s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print (s9 < s9)
print('.')
print (s8 >= s7)
print (s8.issuperset(s7))
print (s8 > s7)
print (s8 > s8)
if s8 >= s7:
    print("it is")

#A la hora de elegir una colección, debemos tener en cuenta sus propiedades.
#Una lista es para guardar multiples objetos o guardar una secuencia
#Un diccionario es para guardar mapeos de clave-valor
#Las tuplas son inmutables
#Los sets son solo para guardar elementos unicos