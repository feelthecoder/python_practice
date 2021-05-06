def count_list_inside_list(l):
    counter=0
    for i in l:
        if type(i)==list:
            counter+=1
    return counter
print(count_list_inside_list([[1,2],[3,4],[],[],[],[],[],[],3,4,6.7,'vikas']))