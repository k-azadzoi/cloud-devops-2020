'''
odd_numbers_list = []

for num in range(1, 10, 3):
    if num % 2 != 0:
        odd_numbers_list.append(num)
        print(f'These are odd numbers {num}')
    else:
        print(f'These are even numbers {num}')


print(odd_numbers_list)
'''




def remove_vowels_from_string(string_to_check):
    vowels = 'aeiou'
    res = ''

    for char in string_to_check:
        if char not in vowels:
            res += char
    return res


print(remove_vowels_from_string("hackerrank"))
