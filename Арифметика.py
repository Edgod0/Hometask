print('Type "qqq" for exit')
while True:
    try:
        sign = input("Chose operation:(+, -, *, /)")
        if sign == "qqq":
            break
        if sign not in ("+", "-", "*", "/"):
            print("Дурак?")
            continue
        a = float(input("a ="))
        b = float(input("b ="))
        if sign == "+":
            print(a + b)
        elif sign == "-":
            print(a - b)
        elif sign == "*":
            print(a * b)
        elif sign == "/":
            print(a / b)
    except ZeroDivisionError as ex:
        print("На ноль делить нельзя")
    except ValueError as e:
        print("Нужно ввести число")
