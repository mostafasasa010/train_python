values = (0, 1, 2)

if any(values):
  # my_var become 0 because values included 1, 2 becouse those are true
  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

# my_list[:4] = true
# my_list[:6] = false
# my_list[:] = false
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
  # print Good because my_list[:4] = true
  print("Good")

else:

  print("Bad")

# Output = Good