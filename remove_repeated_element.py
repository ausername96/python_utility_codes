list_initial=[1,'hi',6,0,5,5,9,'bye','hi']
final_list=[]
repeated_ele=[]
for element in list_initial:
    if list_initial.count(element)==1:
        final_list.append(element)
    else:
        repeated_ele.append(element)
        

print(final_list)
print(repeated_ele)