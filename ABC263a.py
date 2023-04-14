input_list = list(map(int, input().split()))
new_list = list(set(input_list))
fir_count = input_list.count(new_list[0])
sec_count = input_list.count(new_list[1])

if fir_count == 3 and sec_count == 2:
    print("Yes")
elif fir_count == 2 and sec_count == 3:
    print("Yes")
else:
    print("No")
