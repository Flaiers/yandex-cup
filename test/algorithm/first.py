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
    for i in uppers:
        try:
            if uppers[uppers.index(i)+1] == i+1:
                after_upper.append(i)
            elif uppers[uppers.index(i)-1] == i-1:
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

    for i in caps_upper:
        count += 2 + len(i) + 2

print(space + count + len(shift_upper) + len(letters))
