# coding=windows-1251
num1 = float(input("����� ������ �����: "))
num2 = float(input("����� ������ �����: " ))
operator = (input("����� ��������: "))

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
 print("�������� �������� �����!")
