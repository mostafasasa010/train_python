def my_all(list):
  re = True
  for item in list:
    if not item:
      re = False
    else:
      re = True
  return re

def my_any(list):
  re = False
  for item in list:
    if item:
      re = True
  return re

def my_min(list):
  if len(list) < 2:
    return list[0]
  if list[1] < list[0]:
    return my_min(list[1:])
  else:
    return my_min(list[:1] + list[2:])

def my_max(list):
  if len(list) < 2:
    return list[0]
  if list[1] > list[0]:
    return my_max(list[1:])
  else:
    return my_max(list[:1] + list[2:])

# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700