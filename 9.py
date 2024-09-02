L1=[1,2,3,4,5]
L2=[3,4,5,6,7]

Common_Elements=[x for x in L1 if x in L2]
print(Common_Elements)

Non_common_Elements=[x for x in L2 if x  not in L1]
print(Non_common_Elements)