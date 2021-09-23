import requests


url = input()
port = input()
a = input()
b = input()

request = requests.get(f'{url}:{port}', params={'a': a, 'b': b})
data = request.json()

print('\n'.join(map(str, filter(lambda x : x > 0, sorted(data, reverse = True)))))
