age = int(input("Enter Your Age Years: ").strip())
unit = input("Enter Unit From: (Month, Week, Day) ").strip().lower()

if unit == "month": print(f"You Lived {(age * 12):,} Months.")
elif unit == "week": print(f"You Lived {(age * 48):,} Weeks.")
elif unit == "day": print(f"You Lived {(age * 365):,} Days.")
else: print(f"Not Valid Unit")