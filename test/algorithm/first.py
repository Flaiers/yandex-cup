# string = list(input().replace(' ', '')) #  HellO WorlD
string = ['H', 'e', 'l', 'l', 'O', 'W', 'o', 'r', 'l', 'D']

space = string.count(' ')
# lower = sum(map(str.islower, string))
# upper = sum(map(str.isupper, string))

str_list = []

for i in string:
    index = string.index(i)
    str_list.append({index: i})
    print(f'{index} - {i}', 'upper' if i.isupper() else 'lower')
    string[index] = None

print(str_list)
