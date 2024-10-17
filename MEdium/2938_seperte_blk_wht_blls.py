def count_swaps(s):
    zeros = s.count('0')
    count = 0
    ones = 0
    for char in s:
        if char == '0':
            count += ones
        else:
            ones += 1
    return count

s = "0011000010"
result = count_swaps(s)
print(result)