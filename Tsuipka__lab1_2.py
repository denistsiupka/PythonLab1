print("Програма,  змінює значення двох цілих змінних  без використання додаткових змінних.")
num1 = int(input("Введіть num1 = "))
num2 = int(input("Введіть num2 = "))
print(f"num1 = {num1} || num2 = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"num1 = {num1} || num2 = {num2}")
