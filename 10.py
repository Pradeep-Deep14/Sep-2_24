str="ab12cd34"


def separate_elements(str):
    new_str=""
    new_str1=""
    for i in str:
        if i.isdigit():
            new_str+=i
        else:
            new_str1+=i
    return new_str,new_str1

new_str,new_str1=separate_elements(str)

print(f"The new string with numbers is : {new_str}")
print(f"The new string with alphabets is : {new_str1}")