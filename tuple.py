mixed = (1,2,3,4,5,6)

for i in mixed:
    print(i)

num=(1,)
print(num)

num_ ='vikas','sahil','sonia','vishal'
print(num_)


x,y,z = (1,2,3)
print(x,y,z)

list_tuple = ('vikas',['hello','dear'])
list_tuple[1].pop()
print(list_tuple)

lil=(23,4,6,78,554,45,34)
print(min(lil))
print(max(lil))
print(sum(lil))
print(len(lil))

print(tuple(range(1,11)))
string =str(tuple(range(1,11)))
print(list(list_tuple))
print(string[0])

def fun():  #return tuple
    a=30
    n=45
    return a,n

print(fun())


