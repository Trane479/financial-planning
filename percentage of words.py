queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',

]
list = {}

for i in queries:
    words = i.count(' ') + 1
    if words not in list:
        list.setdefault(words, 0)
        list[words] += 1
    else:
        list[words] += 1

print('Распределение запрсоов по количеству слов: ')

sum_words = 0
for counts in list.values():
    sum_words += counts

for words, counts in list.items():
    print(f'Запросов состоящих из {words} слов:{round(counts / sum_words * 100)}%')
