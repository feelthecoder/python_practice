user = {  #dictionary
    'name':'Vikas',
    'age':21
}

nestedUser = {   #dict inside dict
    'name':'Vikas',
    'age':21,
    'new': {
        'name':'Vicky',
        'age':21
    }
}

user1 = dict(name='Vishal',age=18)  #dict function


print(user)
print(user['name'])
print(user1['age'])

print(nestedUser['new'])
print(nestedUser['new']['name'])


#list inside dict

listDict = {
    'list1':[2,4,5,6,7,8,9],
    'list2':[5,8,7,6,5,45,4,5],
    'list3':[45,78,67,554,43,89]
}

print(listDict['list1'])
print(listDict['list1'][5])  #accessing list inside dictionary

#add data to empty dictionary

user_info = {}
user_info['name'] = "Vishal Singh"
user_info['class']= "Intermediate"

print(user_info)


# in and iterations in dictionaries

if 'name' in user_info:
    print("P")

if 'Vishal Singh' in user_info.values():
    print("P")

for i in user_info.values():
    print(i)

for i in user_info:
    print(i)

#Values & Keys in Dictionary

user_values = user_info.values();
print(user_values)

user_keys = user_info.keys();
print(user_keys)

for i in user_keys:
    print(i)
for i in user_values:
    print(i)

#item method

user_items = user_info.items()
print(user_items)

# loop on items

for key,value in user_items:
    print(f"{key} : {value}")

#delete data from dictionary

print(user_info.pop('name'))
print(listDict.popitem())  # return tuple of deleted key-value pair

#update method

more_info = {
    'state': 'Uttar Pradesh',
    'district': 'Mathura',
    'village': 'Nagla Ramtal'
    }

user_info.update(more_info) # add these keys to user_info and replace duplicate keys, if any.
print(user_info)


user_info.update({}) #data remains same
print(user_info)

#constructing dictionary using fromkeys

d= dict.fromkeys(['name','age','city','state'],'NULL')
print(d)

d= dict.fromkeys(('name','age','city','state'),'NONE')
print(d)

d= dict.fromkeys('nacs','none')
print(d)

d= dict.fromkeys(range(5),'empty')
print(d)

d= dict.fromkeys(range(5),[0,0,0,0,0,0,0,0,0,0,0,0]) # any data can be set initially including string.list,tuple,dict,etc.
print(d)


# get method

print(user_info.get('class'))
print(user_info.get('village'))
print(user_info['state'])   #possibility of error in accessing this way.

if user_info.get('age'):  # no need to use in keyword to check presence.
    print("P")
else:
    print("A")

#clear method
d.clear()
print(d)

#copy method
d1 = user_info.copy()  #create a copy
print(d1)

d2 =user_info  #does not create copy but assigns it to d2 hence any action on user_info will affect d2 and vice versa is also true
print(d2)

user_info.popitem()
print(user_info)
print(d2)

d2.popitem()
print(user_info)
print(d2)

# check dictionary are same or not as per memory address

print(d1 is user_info)
print(d2 is user_info)
user_info['district']='Mathura'
user_info['village']='Nagla Ramtal'


# check dictionary are same or not as per key-value pair

print(d1==user_info)
print(d2==user_info)

# get method variant

print(user_info.get('age','Not Available')) # print Not Available instead of None, if key is not present in dictionary


