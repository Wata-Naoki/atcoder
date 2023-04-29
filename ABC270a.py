dic = {
    "1": [1],
    "2": [2],
    "3": [1, 2],
    "4": [4],
    "5": [1, 4],
    "6": [2, 4],
    "7": [1, 2, 4],
}


def cal(input_list, dic):
    result_arr = []
    for val in input_list:
        if val in dic:
            result_arr.extend(dic[val])
        else:
            result_arr.append(val)
    return result_arr


input_list = [n for n in input().split()]
ans_arr = cal(input_list, dic)
print(sum(set(ans_arr)))
