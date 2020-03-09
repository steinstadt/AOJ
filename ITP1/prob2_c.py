# Sorting Three Numbers

# input process
num_list = list(map(int, input().split()))

# sorting process
num_list = sorted(num_list)
num_list = list(map(str, num_list))

# output process
print(" ".join(num_list))
