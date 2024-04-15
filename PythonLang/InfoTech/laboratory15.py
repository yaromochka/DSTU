s = input('Введите строку на английском: ')
s = s.split()
b = []
for i in s:
    b.append(i[0].upper() + i[1::].lower())
print(*b)

