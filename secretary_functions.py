documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


def find_people():
    doc_number = input('Введите номер документа: ')

    for document in documents:
        if document['number'] == doc_number:
            print(document['name'])
            return
    print(f'Документ {doc_number} отсутствует в базе')


def show_document():
    for document in documents:
        print(f'{document["type"]} {document["number"]} {document["name"]}')


def show_shelf(doc_number):
    for directory in directories.items():
        if doc_number in directory[1]:
            return directory[0]
    return f'документ {doc_number} отсутствует на полках'


def add_document():
    doc_number = input('Введите номер нового документа: ')
    doc_type = input('Введите тип нового документа: ')
    name = input('Введите имя: ')
    shelf = input('Введите номер полки, на которой будет храниться документ: ')
    if shelf not in directories:
        print('Данной полки нет в каталоге')

    else:
        documents.append({'type': doc_type, 'number': doc_number, 'name': name})
        for directory in directories:
            if shelf == directory:
                directories[directory].append(doc_number)
    return


def delete_document():
    doc_number = input('Введите номер документа, который хотите удалить: ')

    for document in documents:
        if document['number'] == doc_number:
            documents.remove(document)
            directories[show_shelf(doc_number)].remove(doc_number)
            return
    print('Данный документ отсутствует')


def move_document():
    doc_number = input('Введите номер документа, который хотите переместить: ')
    all_docs = []

    for document in documents:
        all_docs.append(document['number'])

    if doc_number not in all_docs:
        print('Данный документ отсутствует в каталоге')
        return

    shelf = input('Введите номер полки на которую хотите переместить документ: ')

    for directory in directories.values():
        if doc_number in directory:
            directory.remove(doc_number)
    for directory in directories.items():
        if directory[0] == shelf:
            directory[1].append(doc_number)
            return
    i = input('Данная полка отсутствует, хотите ее создать и переместить документ туда?\n')
    if i.lower() == 'да' or 'yes':
        add_shelf(shelf)
        directories[shelf].append(doc_number)


def add_shelf(new_shelf):
    directories.setdefault(new_shelf, [])
    return


def commands_list():
    print('Список всех доступных команд:\n'
          'p - выводит имя человека, которому принадлежит документ\n'
          'l - выводит список всех документов\n'
          's - выводит номер полки, на которой лежит документ\n'
          'a - добавляет документ в каталог и на полку\n'
          'd - удаляет документ из каталога и с полки\n'
          'm - перемещает документ с одной полки на другую\n'
          'as - добавляет новую полку\n'
          )


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            find_people()
        elif command == 'l':
            show_document()
        elif command == 's':
            print(show_shelf(input('Введите номер документа: ')))
        elif command == 'a':
            add_document()
        elif command == 'd':
            delete_document()
        elif command == 'm':
            move_document()
        elif command == 'as':
            add_shelf(input('Введите номер новой полки: '))
        elif command == 'i':
            commands_list()
        elif command == 'exit':
            return
        else:
            print('Команда введена неверно, посмотреть список всех команд - i')


main()


















