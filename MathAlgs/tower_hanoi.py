def hanoi (n, source, target, auxiliary):
    if n > 0:
        hanoi(n-1, source, auxiliary, target)
        if source:
            target.append(source.pop())
        hanoi(n-1, auxiliary, target, source)

source = [1,2,3,4]
target = []
auxiliary = []
hanoi(len(source),source, target, auxiliary)

print(source, auxiliary, target)
