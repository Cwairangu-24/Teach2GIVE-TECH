




def get_max_occurring_char(s):
    """
    Returns the character that appears most frequently in the input string.

    Args:
        s (str): The input string

    Returns:
        str: The most frequent character
    """
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_count = max(char_count.values())
    max_char = [char for char, count in char_count.items() if count == max_count]

    return max_char[0]

str = "sample string"
print("Max occurring character is:", get_max_occurring_char(str))