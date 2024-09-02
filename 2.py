Nested_list=[[1,1,2],[3,3,4,4],5,[6,7,8],9,9]

def flattened_list_remove_duplicates(Nested_list):
    seen=set()
    Flattened=[]
    for element in Nested_list:
        if isinstance(element,list):
            for item in element:
                if item not in seen:
                    Flattened.append(item)
                    seen.add(item)
        else:
            if element not in seen:
                Flattened.append(element)
                seen.add(element)
    return Flattened

print(flattened_list_remove_duplicates(Nested_list))
