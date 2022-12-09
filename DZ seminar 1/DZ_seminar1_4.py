def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        Yes = False
        while not Yes:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                Yes = True
            except ValueError:
                print("Внимание! Увага! ЧИсла джолжны быть целыми!")
    return a
def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment
print("Введите координаты точки А - ")
pointA = inputNumbers(2)
print("Введите координаты точки В - ")
pointB = inputNumbers(2)
print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")