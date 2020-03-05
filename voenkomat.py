age = int(input('Ваш возраст: '))


if 18 <= age < 27:
    print('Вы прошли по возрасту')
    count_of_children = int(input('Введите количество детей: '))
    if count_of_children <= 2:
        print('Количества детей недостаточно для отсрочки')
    else:
        print('Вы не подходите для службы в армии')
        exit(0)
    education_status = input('На данный момент вы обучаетесь в вузе?(да/нет)\n')
    if education_status.lower() == 'да':
        print('Продолжайте обучение и приходите после')
    elif education_status.lower() == 'нет':
        print('Вы подходите для службы в армии')
    else:
        print('Ответ введён некорректно')
else:
    print('Вы не прошли по возрасту')
