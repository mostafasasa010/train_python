myTuple = ("Html", "CSS", "JS")

mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def hello_user(name, *skills, **progSkills):
  print(f"Hello {name} ^_^\nYour Skills Are:")
  for skill in skills:
    print(f"- {skill}")
  print(f"Your Skills With Progress Are:")
  for sName, sValue in progSkills.items():
    print(f"- {sName} => {sValue}")

hello_user("Mostafa", *myTuple, **mySkills)