# Write a function solve that finds the longest palindromic substring in a string.

# Example:
# Input: "babd"
# Output: "bab" 

def solve(s):
  palindrome = ""
  if len(s) < 1:
    return palindrome
  if len(s) == 1:
    return s
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if s[i] == s[j]:
        palindrome = s[i:j+1]
        if i == 0 or j == len(s)-1:
          break
        else:
          if s[i-1] == s[j+1]:
            palindrome = s[i-1: j+1]
  
  return palindrome