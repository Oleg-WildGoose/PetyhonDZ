n = int(input("Введите число n: "))
s = 0
for i in range(1,n+1):
    s += (1+1/i)**i
print(f" для n = {n} Сумма {round(s,2)}")