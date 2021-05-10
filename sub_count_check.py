#Given a function which accept 3 argument. If occurence of the second argument in first argument is equal to the third argument return True else False.

#function maxOccurence(str1: str, str2: str, num: int) -> bool:

def subcount(a,word):
    count=0
    for i in range(len(a)-len(word)):
        if a[i:i+len(word)]==word:
            count+=1
    return count

def maxOccurence(str1:str,str2:str,num:int):
    if subcount(str1,str2)==num:
        return True
    else:
        return False

print(maxOccurence("catzirafecattiger","cat",2))
