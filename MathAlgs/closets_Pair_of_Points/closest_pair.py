# Test Data
# closest_pair([(1, 1), (3, 4), (6, 1), (9, 5), (2, 9)]) should return ((1, 1), (3, 4))
# closest_pair([(0, 0), (10, 10), (5, 5), (-3, -3)]) should return ((0, 0), (-3, -3)) or
# ((5, 5), (-3, -3)) or ((0, 0), (5, 5))

# d=√((x_2-x_1)²+(y_2-y_1)²)

def closest_pair (lists):
    min_pair = ()
    min_distance = 0
    for i in range(len(lists)):
        for j in range(i+1, len(lists)):
            distance = ((lists[j][0] - lists[i][0])**2 + (lists[j][1] - lists[i][1])**2)
            if min_distance == 0 or distance < min_distance:
                min_distance = distance
                min_pair = (lists[i], lists[j])
    return min_pair

# print(closest_pair([(1, 1), (3, 4), (6, 1), (9, 5), (2, 9)]))

print(closest_pair([(0, 0), (10, 10), (5, 5), (-3, -3)]))