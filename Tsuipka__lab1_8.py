print(
    "Програма, яка визначає значення цілої змінної number - від 1 до 7, в залежності від того,\nна який день тижня (від понеділка до неділі) припадає день (ціла змінна day) "
    "невисокосного року, в якому 1 січня - понеділок (1 ≤ day ≤ 365). ")
day = int(input("Введіть номер вашого дня = "))
if day <= 0 or day > 365:
    print("Невірно введені дані")
elif day % 7 == 0:
    print("Неділя")
elif day % 7 == 1:
    print("Понеділок")
elif day % 7 == 2:
    print("Вівторок")
elif day % 7 == 3:
    print("Середа")
elif day % 7 == 4:
    print("Черверг")
elif day % 7 == 5:
    print("П'ятниця")
elif day % 7 == 6:
    print("Субота")
else:
    print("Помилка")