#working example

name,age=input("Enter name and age :").split()
age = int(age)

if (name[0]=='a' or name[0]=='A') and age>10:     #and example
    print("True")
else:
    print("False")

if name=='abc' or age==19:  #or example
        print("True")
else:
    print("False")