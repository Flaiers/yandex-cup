input = input()
string = list(input.replace(' ', ''))

space = input.count(' ')

after_upper = []
next_upper = []
key_upper = []
letters = []

for char in string:
    index = string.index(char)
    key_upper.append(index) if char.isupper() else letters.append(index)
    string[index] = None

for i in key_upper:
    try:
        if key_upper[key_upper.index(i)+3] == i+3:
            after_upper.append(i)
        else:
            next_upper.append(i)
    except IndexError:
        if key_upper[key_upper.index(i)-3] == i-3:
            after_upper.append(i)
        else:
            next_upper.append(i)

print((2 + len(after_upper) + 2 + len(next_upper) if len(after_upper) else len(next_upper)*2) + len(letters) + space)
