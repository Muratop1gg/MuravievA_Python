salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.03  # Ежемесячный рост цен

total_spend = 0

for month in range(1, months + 1):
    if month > 1:
        spend *= increase
    total_spend += spend

money_capital_needed = total_spend - salary * months

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital_needed))
