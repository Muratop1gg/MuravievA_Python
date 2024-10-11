a = 73
b = 10
c = 55

condition_1 = a < 45 < b and c > 45
condition_2 = b < 45 < a and c > 45
condition_3 = c < 45 < a and b > 45

if condition_1 or condition_2 or condition_3:  # TODO объединить три условия с помощью нужного логического оператора and или or
    print("Одно из чисел меньше 45")
