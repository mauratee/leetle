# Write a function solve that implements regular expression matching with support for '.' and '*'. 
# '.' matches any single character, '*' matches zero or more of the preceding element.

# Example:
# Input: "aa", "a*"
# Output: True 

def solve(s, p):
  is_match = False
  for i in range(len(s)):
    for j in range(len(p)):
      if s[i] == p[j] or p[j] in [".", "*"]:
        is_match = True
      else:
        is_match = False
        return is_match
  return is_match

print(solve("aa","a*")) # expect True
print(solve("ab",".*")) # expect True
print(solve("mississippi","mis*is*p*.")) # expect False
print(solve("",".*")) # expect True
print(solve("aab","c*a*b")) # expect True
print(solve("ab",".*c")) # expect False