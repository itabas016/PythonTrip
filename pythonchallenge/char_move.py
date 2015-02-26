def move_char_index(chars, char, new_index):
    # Convert character sequence to list type.
    char_list = list(chars)
    # Get the current index of the target character.
    old_index = char_list.index(char)
    # Remove the target character from the character list.
    char = char_list.pop(old_index)
    # Insert target character at a new location.
    char_list.insert(new_index, char)
    # Convert character list back to str type and return.
    return ''.join(char_list)


chars = 'th i s. i s. a. n i c  ^e . s t r i ng.'
char = '^'

# Move character to the end of the string.
print move_char_index(chars, char, len(chars)) 
# Result: th i s. i s. a. n i c  e . s t r i ng.^

# Move character to the start of the string.
print move_char_index(chars, char, 0) 
# Result:  ^th i s. i s. a. n i c  e . s t r i ng.


def move_char_by_increment(chars, char, increment):
    # Convert character sequence to list type.
    char_list = list(chars)
    # Get the current index of the target character.
    old_index = char_list.index(char)
    # Remove the target character from the character list.
    char = char_list.pop(old_index)
    # Insert target character at a new location.
    new_index = old_index + increment
    char_list.insert(new_index, char)
    # Convert character list back to str type and return.
    return ''.join(char_list)
	
chars = 'th i s. i s. a. n i c  ^e . s t r i ng.'
char = '^'

# Move character forward by 1.
print move_char_by_increment(chars, char, 1) 
# Result: th i s. i s. a. n i c  e^ . s t r i ng.

# Move character backward by 1.
print move_char_by_increment(chars, char, -1) 
# Result: th i s. i s. a. n i c ^ e . s t r i ng. 