def funk():
    a = float(input("введите А="))
    b = float(input("Введите B="))
    if a>b:
        return("Успех")
    if a==b:
        return("Почти")
    if a<b:
        return("Лузер")
print(funk())