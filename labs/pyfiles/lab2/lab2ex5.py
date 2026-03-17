def custom_zip_star(*lists):
    # the asterisk operator allows my zip
    # function to be a variadic function,
    # which can accept a variable number of arguments.

    if not lists: # return empty if lists is empty
        return []

    # minimum length of lists in the list
    min_length = min(len(lst) for lst in lists)

    result = []
    for i in range(min_length):
        row = tuple(lst[i] for lst in lists)
        result.append(row)
        
    return result

list1 = [1,2,3]
list2 = ["mark", "alice", "john", "jane"]
list3 = ["first", "second", "third", "fourth", "fifth"]

listOfTuple = custom_zip_star(list1, list2, list3)
print(listOfTuple)
