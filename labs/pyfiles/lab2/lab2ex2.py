while True:
    try:
        string_count = int(input("How many strings? "))
        break
    except ValueError:
        print("Not an integer. Try again.")

all_strings = []

def delete_duplicate_characters(string):
    result = []
    counts = {}

    # .lower() is used to make detection "uniform"
    # setting how many times each letter appears in the dictionary counts
    for let in string.lower():
        if let in counts:
            counts[let] += 1
        else:
            counts[let] = 1

    # 2nd part of the check: if letter only appears once, keep it
    for let in counts:
        if counts[let.lower()] == 1:
            result.append(let)
    
    return "".join(result)

for i in range(string_count):
    user_input_string = input(f"String {i + 1}: ")
    no_duplicate_char_string = delete_duplicate_characters(user_input_string)
    
    all_strings.append(no_duplicate_char_string)

for word in all_strings:
    print(word)


