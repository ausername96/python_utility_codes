int_list=[1,2,3,4,5,6,7,8,9]
length=len(int_list)

greatest_num=int_list[0]
for element in int_list:
    if element>greatest_num:
        greatest_num=element

print(greatest_num)