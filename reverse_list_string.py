#reverse every string of list and  return that list

def reverse_string_from_list(l):
    reversed=[]
    for i in l:
        reversed.append(i[::-1])
    return reversed

print(reverse_string_from_list(['vikas','durgesh','vishal','sahil']))