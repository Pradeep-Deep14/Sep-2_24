L=[1,2,3,5,6,7]
L1=[]
#L.reverse()
#print(L)

#L1=L[::-1]
#print(L1)

#def reversed_list(L):
#    for i in L:
#        L1.insert(0,i)
#    return L1

#print(reversed_list(L))

for i in range((len(L)-1),-1,-1):
    L1.append(L[i])
print(L1)
