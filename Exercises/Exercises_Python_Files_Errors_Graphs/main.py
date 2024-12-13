#Exercise 1
#f = open('pg37431.txt')
#text = f.read()

#Exercise 2
with open("pg37431.txt") as f:
    print(f.readline())

#Execise 3
#f = open('log.txt','w+')
#from datetime import datetime
#import time
#for i in range(0,10):
    #   print(datetime.now().strftime('%Y%m%d_%H : %M:%S - '),i)
    #f.write(datetime.now().strftime('%Y%m%d_%H : %M:%S - '))
    #time.sleep(1)
    #f.write(str(i))
    #f.write("\n")

#Exercise 4
x = 2
assert x == 2, "Invalid value"


#Exercise 4
def avg(marks):
    assert len(marks) != 0
    return round(sum(marks)/len(marks),2)

sem1_marks = [62, 65, 75]
print("Average marks for semester 1:" ,avg(sem1_marks))
#ranks = []
#print("Average marks for semester 1:" ,avg(ranks))


