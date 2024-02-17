friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
cleaned = []

for text in list(map(lambda li: li[1:-1], friends_map)):
  cleaned.append(text)

print(cleaned)

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"