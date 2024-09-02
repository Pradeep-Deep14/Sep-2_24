L=[1,2,2,3,3,4,5,6,6,7]
L1=[]

def duplicate_list(L):
    for i in L:
        if L.count(i)>1 :
            L1.append(i)
    return L1

print(duplicate_list(L))