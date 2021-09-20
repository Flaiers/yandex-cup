import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

count = 0

for i in s:
    if i in j:
        count += 1

print(count)