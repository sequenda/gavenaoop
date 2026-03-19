def is_palindrome(text):
    text_no_spaces = "".join(text.split())
    reversed = text_no_spaces[::-1]

    if text_no_spaces.lower() == reversed.lower():
        return True
        
    else:
        return False

print(is_palindrome("race car"))
