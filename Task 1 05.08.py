# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.

companies = {}
comp_num = int(input("Введите количество предприятий: "))
for _ in range(comp_num):
    comp_name = input("Введите наименование предприятия: ")
    income = []
    for i in range(4):
        comp_income = int(input(f"Прибыль за {i + 1} квартал: "))
        income.append(comp_income)
    companies[comp_name] = income

companies_list = list(companies.keys())
average_set = []

for i in companies:
    average_set.append(sum(companies[i]) / 4)
    average_all = sum(average_set) / len(average_set)
print(f"Среднее значение прибыли за год среди всех предприятий: {average_all}")

for i in range(len(companies)):
    if average_set[i] > average_all:
        print(f"Предприятие {companies_list[i]} имеет прибыль {average_set[i]}, что выше среднего")
    elif average_set[i] < average_all:
        print(f"Предприятие {companies_list[i]} имеет прибыль {average_set[i]}, что ниже среднего")
