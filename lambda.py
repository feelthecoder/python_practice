#Lambda expression 

# These are one line expressions and don't have any name and are anonymous.

add = lambda a,b:a+b

print(add(5,9))

#We use lambda expressions mostly with advance functions like map,filter,etc

#check whether number is even or not

is_even=lambda num: num%2==0

print(is_even(34))

a = "Vikas"

first = lambda a: a[-1] #last character
upper = lambda a: a.title() #first capital letter

print(first(a))

print(upper(a))

#if-else with lambda

func = lambda s : True if len(s) else False


print(func("Vikas study in rec bijnor"))

