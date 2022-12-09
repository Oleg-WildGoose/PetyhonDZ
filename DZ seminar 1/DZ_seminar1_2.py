def inputKoord(x):
    a = [0] * x
    for i in range(x):
        Yes = False
        while not Yes:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                Yes = True
                if a[i] == 0:
                    Yes = False
                    print("Внимание! Координата не должно быть равна 0. Давай по новой ")
            except ValueError:
                print("Ошибка. Неверные данные при вводе!")
    return a
def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")
koordinate = inputKoord(2)
checkCoordinates(koordinate)