def greater(a,b):
    if a>b:
        return a
    else:
        return b

def new_great(a,b,c):
    bigger = greater(a,b)   #nested function example
    return greater(bigger,c)
print(new_great(10,30,40))