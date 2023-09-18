# coding=windows-1251
num1 = float(input("Введи первое число: "))
num2 = float(input("Введи второе число: " ))
operator = (input("Введи действие: "))

if operator == "+":
 print(num1 + num2)
elif operator == "_":
 print(num1 - num2)
elif operator == "/":
 print(num1 / num2)
elif operator == "*":
 print(num1 * num2)
elif operator == "**":
 print(num1 ** num2)
else:
 print("Неверный оператор ввода!")
