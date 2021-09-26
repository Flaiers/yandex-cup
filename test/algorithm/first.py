count = action = 0; uppers = []; letters = []
input = input(); space = input.count(' ')
string = list(input.replace(' ', ''))

def get_matrix(list):
    matrix = []; row = []
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

if len(letters) and len(uppers):
    letters = get_matrix(letters)
    uppers = get_matrix(uppers)

    for i in letters:
        for j in i:
            if j == 0:
                count += len(i)
                letters.remove(i)

    string = sorted(letters + uppers)

    key_up = False

    for indexes in string:
        if string.index(indexes) % 2:
            if string.index(indexes) + 1 < len(string):
                if len(indexes) >= 4 or (len(indexes) >= 3 and len(string[string.index(indexes) + 1]) <= 2):
                    if key_up:
                        action += 2
                        key_up = False
                else:
                    if key_up:
                        action += len(indexes)
            else:
                if len(indexes) >= 4:
                    if key_up:
                        action += 2
                        key_up = False
                elif string.index(indexes) == len(string) - 1 and len(indexes) >= 3:
                    if key_up:
                        action += 2
                        key_up = False
                else:
                    if key_up:
                        action += len(indexes)
        else:
            if string.index(indexes) + 1 < len(string):
                if len(indexes) >= 4 or (len(indexes) >= 3 and len(string[string.index(indexes) + 1]) <= 2):
                    if not key_up:
                        action += 2
                        key_up = True
                else:
                    if not key_up:
                        action += len(indexes)
            else:
                if len(indexes) >= 4:
                    if not key_up:
                        action += 2
                        key_up = True
                elif string.index(indexes) == len(string) - 1 and len(indexes) >= 3:
                    if not key_up:
                        action += 2
                        key_up = True
                else:
                    if not key_up:
                        action += len(indexes)

        count += len(indexes)

elif len(letters):
    count += len(letters)

elif len(uppers):
    if len(uppers) <= 2:
        action += len(uppers)
        count += len(uppers)
    else:
        action += 2
        count += len(uppers)

print(space + count + action)
