def checkPalindrome(number):
    if int(number)<0:
        return "Number is negative. cant check!!"
    else:
        if number==number[::-1]:
            return "Number is palindrome!!"
        else:
            return "number is not palindrome"
number = input("Enter any number : ")

print(checkPalindrome(number))
