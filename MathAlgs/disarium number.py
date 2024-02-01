def is_disarium_number (num):
    n = num
    sum = 0
    length = len(str(num))
    while (n != 0):
        rem = n % 10
        sum = sum + (rem ** length)
        length = length - 1
        n = n // 10
    if sum == num:
        return True
    else:
        return False

# print(is_disarium_number(89))

for i in range(1, 100000000):
    if is_disarium_number(i):
        print(i)