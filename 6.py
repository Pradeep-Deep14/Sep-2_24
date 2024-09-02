L=[1,2,2,3,3,4,5,6,6,7]
element_count={}

def count_of_elements(L):
    for element in L:
        if element in element_count:
            element_count[element]+=1
        else:
            element_count[element]=1
    return element_count

element_count=count_of_elements(L)

for element,count in element_count.items():
    print(f"The count of {element} is : {count}")