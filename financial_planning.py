monthly_salary = int(input('Введите зарплату за месяц'))
for_mortgage = int(input('Введите процент от зарплаты на ипотеку')) / 100 * monthly_salary
monthly_expenses = int(input('Введите процент от зраплаты на жизнь')) / 100 * monthly_salary
number_of_premium = int(input('Введите количество премий за год'))
premium_amount = number_of_premium * monthly_salary
capital = int((monthly_salary - for_mortgage - monthly_expenses) * 12 + (premium_amount / 2))
mortgage_for_the_year = int(for_mortgage * 12)


print('Было накоплено: ', capital)
print('Потрачено на ипотеку: ', mortgage_for_the_year)



