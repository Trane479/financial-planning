list = ['2018-01-01', 'yandex', 'cpc', 100]
dict = {}
k = len(list) - 1

print(list)
print(k)

for item in reversed(list):
    if item == list[-1]:
        key = list[k - 1]
        value = item
        dict = {key: value}
    else:
        key = item
        value = list[k - 1]
        dict = {key: dict}

print(dict)