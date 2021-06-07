#ENUMERATE

names = ['vikas','sahil','arpit','abhishek']

for pos,name in enumerate(names):   #track position
    print(pos)

#MAP

print(list(map(lambda a:a.title(),names)))

#FILTER

print(tuple(filter(lambda a:True if len(a)<4 else False,names)))

#ZIP

num=[1,2,0,4]
print(list(zip(names,num)))
new_zip=zip(names,num)


# NOTE--> zip object can be converted into dict, list and also zip fucntion can be applied over more than two lists


#Conveting list to dictionary

example=[('a',1),('b',2)]
print(dict(example))

# *operator with ZIP

l1,l2 = list(zip(*new_zip))  # used for unpacking let arguments be [(1,2),(3,4)]
print(l1,l2)

newlist=[]
for pair in zip((2,3,4,5,6,7,8),l2):
    newlist.append(max(pair))

print(newlist)

#make a lambda fucntion taht takes any number of list and return a list which contains average of corresponding list items?

avg = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

print(avg([1,2,3,4,4,5,6],[7,8,9,6,5,4,3],[4,4,5,6,7,8,5]))

# ANY & ALL

print(any(num))
print(all(num))

#MIN & MAX

print(min(num))
print(max(num))
print(min(names,key=len))
print(max(names,key=len))

#SORTED

print(sorted(num)) #short tuple/list and return sorted list
print(sorted(num,reverse=True))  #you can also apply key

#DOC STRING

def fun(a, b):
    '''This is sum function'''
    return a+b;
print(fun(10,45))
print(fun.__doc__)

#HELP

print(help(min))