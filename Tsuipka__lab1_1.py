print("Введіть 4 int числа через пробіл (Максимальна ширина поля:3) = ", end='')
num1, num2, num3, num4 = map(int, input().split())
intformat = '{:<3}'
print(intformat.format(num1), end=" ")
print(intformat.format(num2), end=" ")
print(intformat.format(num3), end=" ")
print(intformat.format(num4))

print("Введіть 2 float числа через пробіл (Максимальна ширина поля:10) = ", end='')
num1, num2= map(float, input().split())
floatformat = '{:<10.2f}'
print(floatformat.format(num1), end=" ")
print(floatformat.format(num2))

str1=input("Введіть рядок (Максимальна ширина поля:2) = ")
strformat="%.2s"
print(strformat % str1)

boolT =True
print(boolT)
