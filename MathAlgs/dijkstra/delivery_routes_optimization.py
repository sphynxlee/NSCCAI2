def read_city_info ():
    city_info = []
    with open('city_info.txt', 'r') as file:
        for line in file:
            city_info.append(line.strip().split(','))
    return city_info