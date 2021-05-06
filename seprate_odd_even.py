def seprate_odd_even(l):
    lil = []
    odd = []
    even = []
    for i in l:
        if i%2==0:
           even.append(i)
        else:
            odd.append(i)
    lil.append(even)
    lil.append(odd)
    return lil


print(seprate_odd_even([1,2,3,4,5,6,7,8,9,8,9,6,66,54,44,3,2323,3,43,4,5,5,65,6,6,777,89]))