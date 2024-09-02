Nested_list=[[1,2,3],[4,5],[6,7,8],9]


def flattened_list(Nested_list):
    Flattened=[]
    for i in Nested_list:
        if isinstance(i,list):
            Flattened.extend(i)
        else:
            Flattened.append(i)
    return Flattened

print(flattened_list(Nested_list))