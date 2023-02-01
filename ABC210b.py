
n = int(input())
s = input()
judge_dict = {0: "Takahashi", 1: "Aoki"}

one_index = s.find("1")
# print(one_index)
print(judge_dict[one_index % 2])
