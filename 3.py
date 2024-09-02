L=[1,2,2,3,3,4,5,6,6,7]

#Remove duplicates and unique elements

def separate_duplicate_and_unique_elements(L):
    seen=set()
    unique_list=[]
    duplicate_list=[]
    for i in L:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
        else:
            duplicate_list.append(i)
    return unique_list,duplicate_list

unique_list,duplicate_list=separate_duplicate_and_unique_elements(L)

print(f"The unique list is : {unique_list} ")
print(f"The duplicate list is : {duplicate_list} ")