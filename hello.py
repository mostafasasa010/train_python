age = input("Enter Your Age Years: ")

age = int(age.strip())
months = age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"""
  Your Count Months Is: {months}
  Your Count Weeks Is: {weeks:,}
  Your Count Days Is: {days:,}
  Your Count Hours Is: {hours:,}
  Your Count Minutes Is: {minutes:,}
  Your Count Seconds Is: {seconds:,}
""")