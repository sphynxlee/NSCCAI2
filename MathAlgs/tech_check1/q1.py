top_secret = ['through', 'day', 'calm', 'vibrant', 'jumping', 'waters', 'energizes', 'reflecting', 'sunlight', 'A', 'keenly', 'ponds', 'frogs', 'near', 'quietly', 'opulent']

def decode_msg (list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

    msg = ' '.join(list)
    return msg

print(decode_msg(top_secret))


