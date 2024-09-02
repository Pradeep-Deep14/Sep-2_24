L1=[1,2,2,3,4,5]
L2=[1,2,3,4,5,6]

def Unique_duplicate(lst):
    return len(lst)==len(set(lst))

print(Unique_duplicate(L1))
print(Unique_duplicate(L2))

