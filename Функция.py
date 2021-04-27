print('Type "qqq" for exit')
while True:
    try:
        def funk():
            if sign == "+":
                return a + b
            elif sign == "-":
                return a - b
            elif sign == "*":
                return a * b
            elif sign == "/":
                return a / b
        sign = input("Chose operation:(+, -, *, /)")
        if sign == "qqq":
            break
        if sign not in ("+", "-", "*", "/"):
            print("Дурак?")
            continue
        a = float(input("a ="))
        b = float(input("b ="))
        print(funk())
    except ZeroDivisionError as ex:
        print("На ноль делить нельзя")
    except ValueError as e:
        print("Нужно ввести число")