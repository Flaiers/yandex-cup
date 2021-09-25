input = input()
string = list(input.replace(' ', ''))
count = input.count(' ')

caps_upper = []
letters = []
uppers = []

def get_matrix(list):
    matrix = []
    row = []
    row.append(list[0])

    for el in range(len(list) - 1):
        if list[el] == list[el + 1] - 1:
            row.append(list[el + 1])
        else:
            matrix.append(row)
            row = []
            row.append(list[el + 1])
    matrix.append(row)

    return matrix

for char in string:
    index = string.index(char)
    uppers.append(index) if char.isupper() else letters.append(index)
    string[index] = None

if len(uppers):
    matrix = get_matrix(uppers)
    for i in matrix:
        if len(i) < 5:
            if i[-1] + 1 in letters:
                for j in i:
                    count += 2
            else:
                caps_upper.append(i)
        else:
            caps_upper.append(i)

    matrix = get_matrix(letters) if len(letters) else []
    if len(caps_upper):
        for n in caps_upper:
            next = n[-1] + 1
            if next in letters:
                count += len(n)
                for i in matrix:
                    if len(i) > 3:
                        if next in i:
                            count += 4
                    elif next in i:
                        count += len(i)
            else:
                count += 2 + len(n)

print(count + len(letters))
