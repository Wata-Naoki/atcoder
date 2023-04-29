def solution(input_list):
    print(input_list)
    duplication_list = []
    for val in input_list:
        if 2 <= input_list.count(val):
            duplication_list.append(val)
    duplication_list = list(set(duplication_list))
    return duplication_list


input_list = list(input())
# num_list = [int(num) for num in input_list]
print(solution(input_list))
# print(num_list)
