# Write a function solve that adds two binary strings and returns their sum as a binary string.
# Example:
# Input: "11", "1"
# Output: "100" 


def solve(a, b):
    result = ''
    carry = 0
    i, j = len(a)-1, len(b)-1
    
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0: total += int(a[i])
        if j >= 0: total += int(b[j])
        result = str(total % 2) + result
        carry = total // 2
        i, j = i-1, j-1
    
    return result

print(solve("11", "1")) # expect "100"
print(solve("1010", "1011")) # expect "10101"
print(solve("0", "0")) # expect "0"
print(solve("1111", "1111")) # expect "11110"