input = input()
string = list(input.replace(' ', ''))

space = input.count(' ')

caps_upper = []
after_upper = []
shift_upper = []
uppers = []
letters = []

for char in string:
    index = string.index(char)
    uppers.append(index) if char.isupper() else letters.append(index)
    string[index] = None

for i in uppers:
    try:
        if uppers[uppers.index(i)+3] == i+3:
            after_upper.append(i)
        else:
            shift_upper.append(i)
    except IndexError:
        if uppers[uppers.index(i)-1] == i-1:
            after_upper.append(i)
        else:
            shift_upper.append(i)

row = []
row.append(after_upper[0])

for i in range(len(after_upper) - 1):
    if after_upper[i] == after_upper[i + 1] - 1:
        row.append(after_upper[i + 1])
    else:
        caps_upper.append(row)
        row = []
        row.append(after_upper[i + 1])
caps_upper.append(row)

# print((2 + len(after_upper) + 2 + len(shift_upper) if len(after_upper) else len(shift_upper)*2) + len(letters) + space)
