n=int(input("Enter Number : "))
total = 0;

while n>0:
    total+=n%10
    n=n//10

print(f"Digits Total : {total}")