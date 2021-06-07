from functools import wraps
import time

def square(a):
    return a*a
s=square
print(s.__name__)
print(square.__name__)

#functions can be passed as an argument and can also be returned

print(list(map(s,[1,2,3,4,5,6,7,8,9])))  #
print(list(filter(lambda a:a%2==0,[1,2,3,4,5,6,7,8,9])))

def squaree(a):  #First CLass Function/ Closure  - function returning function
    def inner():
        print('hello'+str(a*a))
    return inner

var = squaree(10)
var()

#write a program using first class function to calculate square and cube of a number


def to_power(x):
    def rae(n):
        return n**x
    return rae
sq = to_power(2)
cube = to_power(3)

print(sq(5))
print(cube(10))

# Decorators enhance the functionality of other functions

def decorator_fun(any_function):
    def wrapper_function():
        print("This is wrapper")
        any_function()
    return wrapper_function

@decorator_fun
def fun1():
    print('hello')
@decorator_fun
def fun2():
    print('second function')

#fun1 = decorator_fun(fun1)  #normal way of calling decorator
fun1()
fun2()

fun2 = decorator_fun(fun2)

fun2()

#There may occur problems when passing arguments and also when our function is returning some thing.

# Problem of arguments solved

def  decorator_func(any_function):
    def wrapper(*args,**kwargs):
        print("this is awe function")
        return any_function(*args,**kwargs)
    return wrapper

@decorator_func
def func(a):
    print(a)
func(5)

#Problem of function return solved

@decorator_func
def add(a,b):
    return a+b
print(add(5,7))

#one more problem while working with decorators is that when you print name and doc string then it print decorator inner function name and doc string 
#This problem can be solved by using functools library/module

def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        '''this is inner function'''
        print("This is wrapper")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def fun3(a,b):
    '''This is function 3'''
    print(a,b)
    return a+b


print(fun3.__name__)
print(fun3.__doc__)
print(fun3(4,6))

# WAP to create a decorator that will calculate time for function call

def calculate_time(function):
    @wraps(function)
    def time_fun(*args,**kwargs):
        t1=time.time()
        val = function(*args,**kwargs)
        t2 = time.time()
        return val
    return time_fun

@calculate_time
def show_time():
    print("Time is given above")
show_time()

#Decorators with arguments

def only_data_allow(data_type):
    def deco(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return function(*args,**kwargs)
            print("Invalid")
        return wrapper
    return deco

@only_data_allow(str)
def don_con(*arg):
    print(arg)

don_con(1,2,3,4,4,5)

