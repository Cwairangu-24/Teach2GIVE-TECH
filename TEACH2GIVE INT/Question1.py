# Design a function that reverses the digits of an integer. For example, 50
# should become 5 and -12 should become -21.

def reverse_number(num):
    sign = -1 if num < 0 else 1
    reverse_num = int(str(abs(num))[::-1])
    return sign * reverse_num


# Example
print(reverse_number(569))
print(reverse_number(-223))
print(reverse_number(50))