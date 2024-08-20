def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

x = 121
print(isPalindrome(x)) # True