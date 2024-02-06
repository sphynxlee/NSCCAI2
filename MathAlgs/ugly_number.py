# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
# To judge whether a number is ugly, divide by 2, 3, 5 repeatedly.
# But this way is more time-consuming. A better way is to create an array and
# store the ugly numbers.

def GetUglyNumber_Solution(index):
    if index == 0:
        return 0
    result = []
    result.append(1)
    p2 = 0
    p3 = 0
    p5 = 0
    for i in range(index-1):
        v1 = result[p2] * 2
        v2 = result[p3] * 3
        v3 = result[p5] * 5
        min_val = min(v1, v2, v3)
        result.append(min_val)
        if min_val == v1:
            p2 = p2 + 1
        if min_val == v2:
            p3 = p3 + 1
        if min_val == v3:
            p5 = p5 + 1
    ans = result[-1]
    return ans

index = 10
print(GetUglyNumber_Solution(index))