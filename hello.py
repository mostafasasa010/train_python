admins = ["Mostafa", "Ahmed", "Mohamad", "Abdalla", "Mai", "Nada", "Habiba"]

name = input("Enter Your Name Please: ").strip().capitalize()

if name in admins:
  print("You Are Included Admins :)")
  print("Update => U \nDelete => D")
  option = input("Are You Update Or Delete Name? ").strip().capitalize()
  if option == "Update" or option == "U":
    newName = input("Enter Your New Name Please :) ").strip().capitalize()
    admins[admins.index(name)] = newName
    print(f"Thank You :) \nAdmins: {admins}")
  elif option == "Delete" or option == "D":
    admins.remove(name)
    print(f"Done |-_-| \nAdmins: {admins}")
  else:
    print("Option Not Valid")
else:
  print("Your Name Not Included Admins -_-")
  print("Yes => Y \nNo => N")
  addYou = input("Are You Add To Admins? Yes, No: ").strip().capitalize()
  if addYou == "Yes" or addYou == "Y":
    print("Congratulations Add You To Admins :)")
    admins.append(name)
    print(f"Thank You :) \nAdmins: {admins}")
  else:
    print("Your Not Included Admins -_-")