print("Програма,  знаходить середнє арифметичне двох цілих чисел та середнє геометричне двох цілих чисел a і b.;")
num1 = int(input("Введіть num1 = "))
num2 = int(input("Введіть num2 = "))
print(f"num1 = {num1} || num2 = {num2}")

arthAvg = (num1 + num2) / 2
geomgAvg = (num1 + num2) ** 0.5

print(f"Арифметичне середнє = {'{:.1f}'.format(arthAvg)}")
print(f"Геометричне середнє = {'{:.1f}'.format(geomgAvg)}")
