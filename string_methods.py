name = "vikas"
print(len(name)) #length
print("VIKAS".lower()) #make all letters small
print(name.upper()) # make all letters capital
print(name.title()) #make first letter capital
print(name.count('v')) #count number  of letter or string in string
print("   vikas".lstrip()) #remove space from left
print("kumar    ".rstrip())#remove space from right side
print("    vikas   kumar    ".strip())#remove space from left and right but not from mid
print("vikas vikas kumar".replace('vikas','vishal')) # replace vikas with vishal, all occurences
print("vikas vikas vikas kumar".replace('vikas','vishal',2)) # replace vikas with vishal, 2 times
print("vikas kumar".find('kumar'))#return position/index of string
print("vikas kumar".find('ku',2,8)) #return position/index of string starting from given index and ending with index given
print("vikas".center(9,'*'))#put ** on both side 


###String are Immutable and can't be changed once created###






