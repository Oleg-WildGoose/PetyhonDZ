# Изменённая задача 4_2 enimarate

num = int(input("Введите число: "))
i = 2 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
lst = list(enumerate(lst, start=1))
print(f"Простые множители числа {old} приведены в списке: {lst}")