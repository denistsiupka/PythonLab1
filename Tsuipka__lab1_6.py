print(" Програма, допоможе визначачити значення кута в градусах (змінна corner) між станом годинникової стрілки на початку доби ")

hour = int(input('Введіть години (0 < годин < 11) = '))
minute = int(input('Введіть хвилини (0 < хвилин < 59) = '))
second = int(input('Введіть секунди (0 < секунд < 59) = '))
deg_1s = 0.008333333333333333

corner = (float((hour*3600)+(minute*60)+second))*deg_1s

print(f"Градуси = {'{:.1f}'.format(corner)}")