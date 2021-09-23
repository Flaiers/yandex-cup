input = input()
string = list(input.replace(' ', ''))

space = input.count(' ')

upper = []
next_upper = []
key_upper = []
key_lower = []

for char in string:
    index = string.index(char)
    key_upper.append(index) if char.isupper() else key_lower.append(index)
    string[index] = None

for i in key_upper:
    try:
        if key_upper[key_upper.index(i)+1] == i+1:
            upper.append(i)
        elif key_upper[key_upper.index(i)-1] == i-1:
            upper.append(i)
        else:
            next_upper.append(i)
    except IndexError:
        if key_upper[key_upper.index(i)-1] == i-1:
            upper.append(i)
        else:
            next_upper.append(i)

print((2 + len(upper) + 2 + len(next_upper) if len(upper) else len(next_upper)*2) + len(key_lower) + space)
