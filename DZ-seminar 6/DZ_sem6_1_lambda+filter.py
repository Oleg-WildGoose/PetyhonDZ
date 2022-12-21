#модификация задачи семинара 5_1
text = input("Введите текст через пробел:\n")

def del_words (text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = del_words(text)
print(f'после обработки -> {text}')