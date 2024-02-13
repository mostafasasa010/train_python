email = input("Enter Your Email: ")

userName = email.strip().split("@")[0]
emailTag = email.strip().split("@")[1].split(".")[0]

print(f"User Name Is {userName}, Email Tag Is {emailTag}")
