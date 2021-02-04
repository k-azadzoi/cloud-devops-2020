# Create a function to filter the vowels from a string
# Output will be the string with the vowels removed


def remove_vowels_from_string(string_to_check):
    vowels = 'aeiou'
    res = ''

    for char in string_to_check:
        if char not in vowels:
            res += char
    return res


print(remove_vowels_from_string("hackerrank"))