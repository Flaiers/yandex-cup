input = input()
string = list(input.replace(' ', ''))

count = 0
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

if len(uppers):
    for el in uppers:
        i = uppers.index(el)
        try:
            if uppers[i] - uppers[i - 3] == 3 or uppers[i + 3] - uppers[i] == 3:
                if el not in after_upper:
                    after_upper.append(el)
            elif uppers[i + 1] - uppers[i] != 1:
                if el not in after_upper:
                    shift_upper.append(el)
            elif uppers[i] - uppers[i - 2] == 2:
                if el not in after_upper:
                    after_upper.append(el)
            else:
                if el not in after_upper:
                    shift_upper.append(el)
        except IndexError:
            if uppers[i] - uppers[i - 3] == 3:
                if el not in after_upper:
                    after_upper.append(el)
            else:
                if el not in after_upper:
                    shift_upper.append(el)

    if len(after_upper):
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

        for i in caps_upper:
            count += 2 + len(i) + 2

print(space + count + len(shift_upper)*2 + len(letters))
