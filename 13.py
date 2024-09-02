#Count of Elements in List

L = [1, 2, 'abc', 2, 66, 'abc', 66, 66, 99, 'abc']

def count_elements(L):
    L1=[]
    for i in L:
        if i not in L1:
            L1.append(i)
    return len(L1)

print(count_elements(L))