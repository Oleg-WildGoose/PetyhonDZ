def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            print(f"на нечётных позициях элементы {s}")
            s += lst[i]
    print(f"ответ: {s}")
lst = [1, 1, 1, 1, 1]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)