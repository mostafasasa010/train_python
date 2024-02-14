tries = 3

password = "mostafa010"

inputPass = input("Enter Your Password: ")

while inputPass != password:
  if inputPass == password:
    break
  tries -= 1
  print(f"Wrong Password!, {'Last' if tries == 0 else tries} Avilable Try -_-")
  inputPass = input("Enter Your Password: ")
  if tries == 0:
    print("Wrong Password!\nDon't Have Tries. -_-")
    break
else:
  print("Correct. :)")