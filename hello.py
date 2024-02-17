i = 1
while i <= 20:
  if i == 6 or i == 8 or i == 12:
    i += 1
  print(f"0{i}" if i < 10 else f"{i}")
  i += 1
else:
  print("All Numbers Printed")

# Needed Output
# "01"
# "02"
# "03"
# "04"
# "05"
# "07"
# "09"
# "10"
# "11"
# "13"
# "14"
# "15"
# "16"
# "17"
# "18"
# "19"
# "20"
# "All Numbers Printed"