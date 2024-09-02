L=[1,2,2,3,3,4,5,6,6,7]
L1=[]

def unique_elements(L):
    for i in L:
        if i not in L1:
            L1.append(i)
    return L1

print(unique_elements(L))