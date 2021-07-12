#generator function
def nums(n):
    for i in range(1,n+1):
        yield(i)

for number in nums(10):
    print(number)

#generators printed once only, can be converted to list
#generators takes less memory and less time as compared to list ds

#generator comprehension

square = (i**2 for i in range(1,11))

for i in square:
    print(i)

for i in square: # you can use generator only once 
    print(i)


#Since generators are iterators , you can use next(square) function directly to get next elements.