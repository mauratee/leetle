# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
        stack = []
        for char in s:
            print(char)
            if char in "([{":
                stack.append(char)
                print(stack)
            else:
                if not stack:
                    print("not stack")
                    return False
                if char == ")" and stack[-1] != "(":
                    print("not )")
                    return False
                if char == "]" and stack[-1] != "[":
                    print("not ]")
                    return False
                if char == "}" and stack[-1] != "{":
                    print("not }")
                    return False
                open = stack.pop()
        print(stack)
        return not stack

print(isValid("()[]{}"))