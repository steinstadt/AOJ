# 最大値、最小値、合計

# input process
n = int(input())
a_list = list(map(int, input().split()))

# operation
min_num = min(a_list)
max_num = max(a_list)
sum_num = sum(a_list)

print("%d %d %d"%(min_num, max_num, sum_num))
