peoples = {
  "Mostafa": {
    "Html": "100%",
    "Css": "90%",
    "Js": "100%",
    "Python": "80%",
  },
  "Ahmed": {
    "Html": "100%",
    "Css": "90%",
    "Python": "80%",
    "C++": "90%",
  },
  "Ali": {
    "Html": "100%",
    "Css": "90%",
    "PHP": "70%",
    "C": "50%",
    "Go": "20%",
  }
}

for person in peoples:
    print(f"The {person} Skills Are: ")
    for skill in peoples[person]:
      print(f"- Skill Is {skill.upper()}: {peoples[person][skill]} Progress.")