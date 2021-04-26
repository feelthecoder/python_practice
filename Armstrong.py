def Armstrong(lower,upper):
    for num in range(lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            return(num)

l=100
u=999
print(Armstrong(l,u))