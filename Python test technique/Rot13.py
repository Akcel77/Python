def rot13(text):
    result = ""

    # Loop for each char
    for char in text:
        # Convert to number with ord
        char_ord = ord(char)

        # Back or forward
        if char_ord >= ord('a') and char_ord <= ord('z'):
            if char_ord > ord('m'):
                char_ord -= 13
            else:
                char_ord += 13
        elif char_ord >= ord('A') and char_ord <= ord('Z'):
            if char_ord > ord('M'):
                char_ord -= 13
            else:
                char_ord += 13

        # Add to result
        result += chr(char_ord)

    # Return
    return result


# Test
print(rot13("Ceci est un test"))
print(rot13(rot13("Ceci est un test")))
