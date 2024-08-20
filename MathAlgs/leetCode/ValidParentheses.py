def isValidParentheses(str):
    closeToOpen = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in str:
        if char in closeToOpen:
            if not stack or stack.pop() != closeToOpen[char]:
                return False
        else:
            stack.append(char)

    return True if not stack else False

str = '([{}])'
print(isValidParentheses(str)) # True