# Write a function solve that finds all elements that appear more than n/3 times in an array.

# Example:
# Input: [3,2,3]
# Output: [3] 

def solve(nums):
  majority = len(nums)/3
  counts = {}
  major_elements = []
  for elem in nums:
    if elem in counts:
      counts[elem] += 1
    else:
      counts[elem] = 1
  for key in counts:
    if counts[key] > majority:
      major_elements.append(key)
  
  return major_elements

print(solve([3,2,3])) # expect [3]
print(solve([1])) # expect [1]
print(solve([1,2])) # expect [1,2]
print(solve([2,2,1,1,1,2,2])) # expeect [2,1]
print(solve([])) # expect []
print(solve([8,8,8,8,9])) # expect [8]