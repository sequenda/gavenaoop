def remove_duplicates(items):
    no_duplicates_list = []
    
    for item in items:
        if item not in no_duplicates_list:
            no_duplicates_list.append(item)
        else:
            continue

    return no_duplicates_list

