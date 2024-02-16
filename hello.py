# Assignment from 60 to 64

# Assignment Three
scores_list = {
  "Math": 90,
  "Science": 80,
  "Language": 70
}
def get_the_scores(name = None, **scores_list):
  def scoresLoop(scores_list):
    for scoreK, scoreV in scores_list.items():
      print(f"{scoreK} => {scoreV}")
  if name and scores_list:
    print(f"Hello {name} This Is Your Score Table:")
    scoresLoop(scores_list)
  elif name and scores_list == {}:
    print(f"Hello {name} You Have No Scores To Show")
  elif name == None and scores_list:
    scoresLoop(scores_list)

# Test 1
get_the_scores("Osama", **scores_list)

# Output
# "Hello Osama This Is Your Score Table:"
# "Math => 90"
# "Science => 80"
# "Language => 70"

# Test 2
get_the_scores("Osama")

# Output
# "Hello Osama You Have No Scores To Show"

# Test 3
get_the_scores(**scores_list)

# Output
# "Math => 90"
# "Science => 80"
# "Language => 70"