# Assignment from 60 to 64

# Assignment One
def get_score(**techs):
  for techKey, techVal in techs.items():
    print(f'"{techKey} => {techVal}"')

get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)