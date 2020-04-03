def calc(expression):
    operator = []
    operands = []
    result = []
    for item in expression:
        math_sign = ['+', '-', '*', '/']
        assert expression[0] in math_sign, 'Операции не найдено!'
        try:
            if item.isalpha():
                raise AssertionError
        except AssertionError:
            return 'Нужно вводить числа'
        if item.isdigit():
            try:
                if len(operator) == 0:
                    raise AssertionError
            except AssertionError:
                return 'Первым должент быть  оператор'
            operands.append(item)
        else:
            operator.append(item)
        for blanks in operator:
            if blanks == ' ':
                operator.remove(blanks)
    try:
        if not len(operands) > 1:
            raise AssertionError
    except AssertionError:
        return 'Введите два положительных числа'

    operator = operator[0]
    if operator == '+':
        result = int(operands[0]) + int(operands[1])
    elif operator == '-':
        result = int(operands[0]) - int(operands[1])
    elif operator == '*':
        result = int(operands[0]) * int(operands[1])
    elif operator == '/':
        try:
            result = int(operands[0]) / int(operands[1])
        except ZeroDivisionError:

            return 'Делить на ноль нельзя'
    return result


def main():

    while True:
        expression = input('Введите данные: \n').split()
        if expression[0] == 'e':
            break
        print(calc(expression))


main()


