skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
i = 0

def reverseTuple(t):
  newTuple = t[::-1]
  return newTuple

newSkills = reverseTuple(skills)

while i < len(newSkills):
  if type(newSkills[i]) == str:
    print(f"{newSkills.index(newSkills[i]) + 50} - {newSkills[i]}")
  i += 1

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"