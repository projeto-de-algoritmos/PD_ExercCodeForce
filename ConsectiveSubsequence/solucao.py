def find_sequence_length(n, sequence):
    counter_dict = {}
    for num in sequence:
        counter_dict[num] = counter_dict.get(num - 1, 0) + 1

    last_num = max(counter_dict, key=counter_dict.get)
    sequence_length = counter_dict[last_num]

    first_num = last_num - sequence_length + 1
    j = 0
    temp_indexes = []

    while first_num <= last_num:
        if sequence[j] == first_num:
            temp_indexes.append(j)
            first_num += 1
        j += 1

    sequence_indexes = [temp_indexes[i] + 1 for i in range(sequence_length)]

    return sequence_length, sequence_indexes

n = int(input())
sequence = list(map(int, input().split(' ')))

length, indexes = find_sequence_length(n, sequence)

print(length)
print(' '.join(str(i) for i in indexes))