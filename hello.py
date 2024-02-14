listOfMovies = []
countMovies = int(input("Enter Count Save Movies: ").strip())

while countMovies > 0:
  nameMovie = input("Name Movie: ").strip().capitalize()
  listOfMovies.append(nameMovie)
  countMovies -= 1
  print(f"List Of Movies: {listOfMovies}\nAvilable Places Is: {countMovies}")
else:
  listOfMovies.sort()
  print("Thanks Pro :)")
  print(f"List Movies Is:\n{listOfMovies}")