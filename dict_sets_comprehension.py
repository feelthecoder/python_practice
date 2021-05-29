# Dictionary comprehension used to create dictionary in one line

square = {num:num**2 for num in range(1,11)}  # Dictionary of key square
print(square)

#create a dictionary of character count of a string

String = "Vikas is a good programmer"

dict_count = {i:String.count(i) for i in String}
print(dict_count)

#dict comprehension with if else

odd_even = {i: ('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)


# Set comprehension used to create set in one line

s= {k**2 for k in range(1,11)}
print(s)