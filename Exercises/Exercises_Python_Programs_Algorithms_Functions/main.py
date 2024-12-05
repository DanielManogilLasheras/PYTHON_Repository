
import math
#Exercise One
def compute(numbers):
    return([math.factorial(n) for n in numbers])


math.exp(2)

from math import exp
exp(2)

from math import * #Avoid unless necessary

import datetime
print(datetime.date.today())

#Exercise 2
def sum_to_10():
    result = 0
    for n in range(1,10):
        result += n
    if __name__ == '__main__':
        print(result)

#Exercise 3
def tell_me_time():
    """
    :return: This script return the current system time
    """
    import datetime
    time = datetime.datetime.now().time()
    if __name__ != '__main__':
        print(time)

#Exercise 4
def maximum(numbers):
    maximum = 10
    for n in numbers:
        if n>maximum:
            print(n , "number is bigger than" , maximum)

#Exercise 5
def sortArray(array):
    still_swapping = True
    while still_swapping:
        still_swapping = False
        for n in range(len(array) - 1):
            if array[n] > array[n + 1]:
                array[n] , array [n + 1] = array[n+1] , array [n]
                still_swapping = True
            print(array)

#Exercise 6
def linearSearch():
    l = [5,1,8,3,2]
    search_for = 8
    result = -1
    for i in range(len(l)):
        if search_for == l[i]:
            result = i
            break
    print (result)

def binarySearch():
    l = [2,3,5,8,11,12,18]
    search_for = 11
    slice_start = 0
    slice_end = len(l) - 1
    found = False

    while slice_start <= slice_end and not found:
        location = (slice_start + slice_end) // 2
        if l[location] == search_for:
            found = True
        else:
            if search_for < l[location]:
                slice_end = location - 1
            else:
                slice_start = location + 1
        print(found)
        print(location)

#Exercise 7
def list_product(my_list):
    result = 1
    for number in my_list:
        result *= number
    return result


#Exercise 8
def add_sufix(suffix='.com'):
    return 'google' + suffix

def convert_usd_to_aud(amount, rate=0.75):
    return amount / rate

print(convert_usd_to_aud(100))

#Exercise 9
def convert_usd_to_aud(amount , rate):
    return amount / rate ;
def convert_and_sum_list(usd_list, rate = 0.75):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, rate=rate)
    return total
print(convert_and_sum_list([1, 3]))
def convert_and_sum_list_kwargs(usd_list, **kwargs):
    total = 0
    for amount in usd_list:
        total += convert_usd_to_aud(amount, **kwargs)
    return total
#Los diccionarios kwargs son funcions que nos permiten aceptar cualquier argumento keyword cuando se llaman
#Estos pueden ser accedidos en un diccionario kwargs
#print(convert_and_sum_list_kwargs([1,3], rate=0.8))

def format_customer(name,surname,location= None):
    full_name = '%s %s' % (name, surname)
    if location:
        return '%s (%s)' % (full_name,location)
    else:
        return full_name

print(format_customer('John', 'Smith', location='California'))
print(format_customer('Mareike' , 'Schmidt'))


#Exercise 10
def is_prime(x):
    for i in range (2,x):
        if(x % i) == 0:
            return False
    return True
print(is_prime(1000))

#Exercise 11
def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current
print(fibonacci_iterative(10))

def countdown(n):
    if n == 0:
        print('liftoff!')
    else:
        print(n)
        return countdown(n - 1)
countdown(3)