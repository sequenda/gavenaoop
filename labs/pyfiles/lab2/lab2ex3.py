def vowelsToUpper(string):
    result = []

    for let in string:
        if let.lower() in 'aeiou':
            result.append(let.upper())
        else:
            result.append(let)
    
    return "".join(result)

user_string = input("Test: ")
print(vowelsToUpper(user_string))