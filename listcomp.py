#list comprehension allow us to create list in one line

#list of square from 1 to 10

list = [i*i for i in range(1,11)]
print(list)

#create list of negative number from 1 to 10

lil_n = [-i  for i in range(1,11)]
print(lil_n)

#create first letter list
names=["Vikas","Arpit","Abhishek","Pawan"]
listHeader=[name[0] for name in names]
print(listHeader)

#create a new list by reversing each string in list

old_list = ["vikas","recbijnor","dscrecbijnor","bijnor","mathura"]
new_list = [name[::-1] for name in old_list]
print(new_list)


## List comprehension with if statement
#given a list create new list of even numbers

numbers =[1,2,3,4,5,6,7,8,9,10]
even_num =[i for i in numbers if i%2==0]
print(even_num)

#define a function which takes list as input and returns a list which contains numbers only as a string

def convert(l):
    return [str(i) for i in l if(type(i)==int or type(i)==float)]

print(convert([1,2,'hello',3.0]))

# if-else with list comprehension

new_list = [i*2 if(i%2==0) else -i for i in range(1,11)]

print(new_list)

#Nested list comprehension

#nested_list =[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]

lis = [[i for i in range(1,10)] for j in range(3)]
print(lis)

