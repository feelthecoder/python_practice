def is_palin(palin):
     return (palin==palin[::-1])

strr=input("Enter to check:")
print(f"It is palindrome :{is_palin(strr)}")