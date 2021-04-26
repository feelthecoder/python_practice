stri=input()
x=""
A=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
stri=stri.lower()
for i in stri:
    ext=27
    for j in A:
        ext-=2
        if i==j:
         x+=chr(97+int(A.index(i))+ext)
        elif i==" ":
         x+=" "
print(x)
