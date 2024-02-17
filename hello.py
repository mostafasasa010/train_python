# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
result = 0

for rankKey, rankValue in my_ranks.items():
  val = 0
  if rankValue == "A":
    result += 100
    val = 100
  elif rankValue == "B":
    result += 80
    val = 80
  elif rankValue == "C":
    result += 40
    val = 40
  print(f"My Rank in {rankKey} Is {rankValue} And This Equal {val} Points")
else:
  print(f"Total Points Is {result}")

# Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"