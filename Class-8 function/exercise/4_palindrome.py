def palindrome_check(text):
    # text[::-1] is a simple Python trick to reverse a string
    reversed_text = text[::-1]
    
    # Check if the original text is the same as the reversed text
    if text == reversed_text:
        return True
    else:
        return False

# Testing the function
print(palindrome_check("madam"))   # Output: True
print(palindrome_check("python"))  # Output: False
print(palindrome_check("racecar")) # Output: True





def palindrome_check_loop(text):
    # Start with an empty string
    reversed_text = ""
    
    # Loop through each character in the original text
    for char in text:
        # Add the new character to the FRONT of the reversed_text
        reversed_text = char + reversed_text
        
    if text == reversed_text:
        return True
    else:
        return False

# Testing the function
print(palindrome_check_loop("python"))  # Output: False