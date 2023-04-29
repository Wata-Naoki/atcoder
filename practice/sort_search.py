def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1


input_origin_list = [9, 1, 2, 3, 4, 5, 6, 7]
input_list = input_origin_list
input_list.sort()
target = int(input())

result = binary_search(input_list, 0, len(input_list) - 1, target)
if result != -1:
    ans = input_origin_list.index(result)
    print("元のリストでは{}番目にある".format(ans + 1))
    print("指定された要素はリストの{}番目にあります".format(result + 1))
else:
    print("要素内に存在しない")
