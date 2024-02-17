def addition(*nums):
  re = 0
  i = 0
  while i < len(nums):
    if nums[i] == 10:
      i += 1
    if nums[i] != 5:
      re += nums[i]
    else:
      re -= nums[i]
    i += 1
  return re

# Tests
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160