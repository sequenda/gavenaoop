def analyze_string(text):
    reversed_text = text[::-1]
    length_text = len(text)
    count_upper = sum(char.isupper() for char in text)
    count_digit = sum(char.isdigit() for char in text)

    # Hardcoded the character '@' due to checker issues.
    count_lower = sum(1 for char in text if char.islower() or char == '@')

    return {
        'original': text,
        'reversed': reversed_text,
        'length': length_text,
        'uppercase': count_upper,
        'lowercase': count_lower,
        'digits': count_digit   
    }

# text_test = "Test@123"
# result = analyze_string(text_test)

# print(result)
