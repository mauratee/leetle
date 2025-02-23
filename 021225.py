# Write a function solve that divides two integers without using multiplication, division, and mod operator. 
# Return the quotient as an int after dividing. Assume 32-bit signed integers.

# Example:
# Input: 10, 3
# Output: 3 

def solve(dividend, divisor):
  quotient = 0
  remainder = dividend
  negative = False
  if divisor == dividend:
    return 1
  if divisor > dividend:
    return quotient
  if divisor < 0:
    negative = True
  for i in range(dividend):
    if remainder >= abs(divisor):
     quotient +=1
     remainder -= abs(divisor)
  if negative:
    return -quotient
  return quotient

print(solve(10,3)) # expect 3
print(solve(7, -3)) # expect -2
print(solve(100,1)) # expect 100
print(solve(0,1)) # expect 0
print(solve(1,1)) # expect 1
print(solve(1,2)) # expect 0