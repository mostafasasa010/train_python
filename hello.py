friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
names = []

for name in list(filter(lambda text: text[-1] == "m", friends_filter)):
  names.append(name)

for name in names:
  print(name)

# Output
# "Wessam"
# "Essam"