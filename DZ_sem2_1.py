def InputNumbers(inputText):
    Yes = False
    while not Yes:
        try:
            number = float(input(f"{inputText}"))
            Yes = True
        except ValueError:
            print("Это не число!")
    return number
def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum
num = InputNumbers("Введите число: ")

print(f"{num} -> {sumNums(num)}")