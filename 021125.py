# Write a function solve that finds the length of the longest substring without repeating characters.
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. 

def solve(s):
    maxlength = 1
    if s == '':
        return 0
    substring = ""
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1, len(s)):
            if s[j] not in substring:
                substring = substring + s[j]
                maxlength = max(maxlength, len(substring))
            else:
                break
    return maxlength
