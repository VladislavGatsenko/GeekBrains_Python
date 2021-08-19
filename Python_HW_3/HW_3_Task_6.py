def capitalize(line):
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))


line = input("Введите слова в lower case через пробел: ")
print(capitalize(line))
