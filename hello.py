def calculate(n1, n2, calc = "add"):
  calc = calc.lower()
  if calc == "add" or calc == "a" or not calc:
    return n1 + n2 
  elif calc == "subtract" or calc == "s":
    return n1 - n2
  elif calc == "multiply" or calc == "m":
    return n1 * n2
  else:
    return f"{calc} Not Valid"


# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200