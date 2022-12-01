import random
lst = [random.randint(0,10) for i in range(random.randint(0,10))]
print(f"исходный список:\n{lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")