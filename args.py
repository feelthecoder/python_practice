#add any number of elements
#take parameters as tuple *kwarg

def total(*args):
    tot=0
    for i in args:
        tot+=i
    return tot

print(total(12,3,4,5,5,6,67,7,78,8,8))

#if passing a list then must use * operator while passing to unpack values

#also put *args always in the end of all arguments

# DOUBLE STAR OPERATOR  
#takes parameters as dictionary
#if passing a dictionary then use ** to unpack values


def func(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

func(first="Vikas",last="Kumar")

