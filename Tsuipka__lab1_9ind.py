import math

print("Ця програма, яка допоможе за довжинами двох сторін деякого трикутника АВС і кута (в градусах) між ними\nзнаходити"
      " довжину третьої сторони і площу цього трикутника.\n")
print("Пошук третьої сторони А виконується за допомогою теореми косинусів")
print("Пошук площі трикутника АВС виконується за допомогою формули Герона (напівпериметра)\n")

side_B = float(input("Введіть сторону B = "))
print(f"Cторонa B = {'{:.1f}'.format(side_B)}")

side_C = float(input("Введіть сторону C = "))
print(f"Cторонa C = {'{:.1f}'.format(side_C)}")

deg = float(input("Введіть кут AB (в градусах) між ними = "))
print(f"Kут AB (в градусах) = {'{:.1f}'.format(deg)}")
# Всі тригонометричні функції оперують радіанами.
rad = math.radians(deg)
cos_side = math.cos(rad)

sumAB = side_B ** 2 + side_C ** 2
cosAB = 2 * (side_B * side_C) * cos_side

side_A = (sumAB - cosAB) ** 0.5
print(f"\nCторонa A = {'{:.1f}'.format(side_A)}")

p=(side_A+side_B+side_C)/2
S=math.sqrt(p*((p-side_A)*(p-side_B)*(p-side_C)))
print(f"Площа трикутника ABC = {'{:.1f}'.format(S)}")
