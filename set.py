s={1,2,3,2}
print(s)  #Indexing cannot be used

#remove duplicates from list

list1=[1,4,5,6,7,8,9,3,4,5,6,2]
set_new= set(list1) 
print(set_new)

list2= list(set_new)
print(list2)

#methods of set
s.add(7)
s.add(6)
print(s)
s.remove(2) #give KeyError if not present
print(s)
s.discard(2) #simpley remove else not give error
print(s)
s1=s.copy()
print(s1)
s1.clear()
print(s1)


#set cannot store list,tuple,dictionary but can store any other type like integer,floating,string

if 7 in s:
    print("present")
else:
    print("Not present")

#sets are unordered hence can print its value in any order

for item in s:  #loop in sets
    print(item)

# union and intersection operation
s1={1,3,4,5,6,7}
s2={3,4,5,6,9,2}
print(s1|s2)
print(s1&s2)