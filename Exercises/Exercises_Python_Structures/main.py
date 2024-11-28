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
