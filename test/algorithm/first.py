input = input()
string = list(input.replace(' ', ''))

space = input.count(' ')

key_upper = []
key_lower = []
str_list = []

for i in string:
    index = string.index(i)
    str_list.append({index: i})
    key_upper.append(index) if i.isupper() else key_lower.append(index)
    string[index] = None

print(len(key_upper)*2 + len(key_lower) + space)
