n = int(input("Введите число для преобразовывания в двоичное: "))
s = " "
while n != 0:
    s = str(n%2) + s
    n //=2
print(f"-> {s}")