boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = sorted(boys)
girls = sorted(girls)
matches = list(zip(boys, girls))


if len(boys) != len(girls):
    print('Разное количество мальчиков и девочек')
else:
    print('Идеальные пары:')
    for boy, girl in matches:
        print(f'{boy} и {girl}')
