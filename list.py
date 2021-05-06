lil = [1,2,3,4,5,6,7,8,9]
list1 = [90,80]

print(lil[2])  #indexing
print(lil[:2]) #slicing

lil[6]=78

lil.append(80)
lil.insert(3,99)
lil.extend(list1)
print(lil)
lil.append(list1)
print(lil)
print(lil+list1)
print(lil)
print(lil.pop())
print(lil.pop(2))
print(lil)
del lil[2]
print(lil)
lil.remove(80)
print(lil)
#lil.remove(8909)  #error will occur
#print(lil)

if 91 in lil:
    print("Present")
else:
    print("Not Present")

lil.append(80)
lil.append(80)
lil.append(80)

print(lil.count(80))
lil.sort()
print(lil)

#lil.sort(reverse=True)
#print(lil)

print(sorted(lil))
print(lil)
list2= lil.copy()
#lil.clear()
print(lil)
print(list2)

if lil==list2:
    print("EQUAL")
else:
    print("NOT EQUAL")

print(list2 is lil)

user_info = "Vikas 29 Mathura 9536516618 REC".split()
print(user_info)

string=['vikas','is','good']

print(','.join(string))

for number in lil:
    print(number)

i=0

while i<len(lil):
    print(lil[i])
    i+=1


matrix =[[1,3,5],['vikas','hello','mathura'],[3.4,'vikas',5,7,8],[1,2,3,4,5,6,7,8,9]]

for i in matrix:
    for j in i:
        print(j)



print(type(list2))

numbers= list(range(1,50,2))
print(numbers)
print(numbers.index(5))
print(numbers.index(5,1))
print(numbers.index(5,2,10))
print(max(list2))
print(min(list2))


#printing negative list from a positive list

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list([1,7,5,9,34,56,90,34,32]))
