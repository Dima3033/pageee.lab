counter = 0
txt = input(" Введіть текст ->")
words = txt.split()
for word in words:
    if txt.count(word) > 0:
        im = txt
        temp = txt[0].upper() + txt[1:]
        txt = txt.replace(im, temp)
print(txt)
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string = input(' num ->')
for i in string:
    if i in digits:
        counter += 1
print('Кількість цифр у тексті', counter)
digits = ['!', '?', '+', ':', ',', '-', ';', '*']
string = input('Symbol ->')
for i in string:
    if i in digits:
        counter += 1
print('Кількість символів у тексті', counter)