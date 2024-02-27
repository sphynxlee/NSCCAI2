import os
file_path = os.getcwd() + '/NSCCAI2/MathAlgs/dijkstra/city_info.txt'

def read_city_info ():
    city_info = []
    with open(file_path, 'r') as file:
        for line in file:
            city_info.append(line.strip().split(','))
    return city_info

print(read_city_info())