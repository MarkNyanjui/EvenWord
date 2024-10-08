def even_word(S):
    N = len(S)
    char_counts = {}
    odd_count = 0

    if not N > 0 or N < 200000:
        print("Length of string must be in range of 0 and 200000")
    
    for char in S:
        if not char.isalpha() or not char.islower():
            print("Characters must be lowercase letters")
        else:
            char_counts[char] = char_counts.get(char, 0) + 1

    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count

print(even_word("aaaabbbbcccc")) # Expected output -> 0
print(even_word("abcdef")) # Expected output -> 6
print(even_word("wwwxxxyyyzzz")) # Expected output -> 4