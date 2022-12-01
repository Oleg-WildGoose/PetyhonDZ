N = int(input("Введите N "))
lst = [1]
for i in range(2, N+1):
    lst.append(lst[i-2] * i)
print(f"Итоговый набор {lst}")