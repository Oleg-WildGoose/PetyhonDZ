def InputNumbers(inputText):
    Yes = False
    while not Yes:
        try:
            number = int(input(f"{inputText}"))
            Yes = True
        except ValueError:
            print("Это не число!")
    return number
def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes, yes, yes!")
    elif 0 < num < 6:
        print("Naen, naen, naen!")
    else:
        print("число не является днём недели")
num = InputNumbers("Введите число: ")
checkNumber(num)