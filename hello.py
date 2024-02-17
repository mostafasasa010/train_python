from functools import reduce

nums = [2, 4, 6, 2]

num = reduce(lambda n1, n2: n1 * n2, nums)

print(num)

# Output
# 96