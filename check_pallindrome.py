def check_pallindrome(sen):
    revrs_list=[]
    index=-1
    for element in range(1,len(sen)+1):
        revrs_list.append(sen[index])
        index=index-1
    revrs_sentence="".join(revrs_list)
    if sen==revrs_sentence:
        print(f"{sen} is pallindrome")
    else:
        print(f"{sen} is not pallindrome")

sentence="uwu"
check_pallindrome(sentence)