# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]
i = 1

for num in sorted(my_nums, reverse=True):
  if num % 5 == 0:
    print(f"{i} => {num}")
    i += 1
else:
  print("All Numbers Printed")

# Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"