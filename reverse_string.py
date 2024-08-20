string="letter"

letters=[]
reverse_letters=[]
for elements in string:
    letters.append(elements)
    
a=-1
for elements in letters:
     reverse_letters.append(letters[a])
     a=a-1
     
print("".join(reverse_letters))
