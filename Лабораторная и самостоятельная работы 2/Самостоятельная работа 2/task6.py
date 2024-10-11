list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

el_value = 0

el_index = 0

for i, num in enumerate(list_numbers):
    if el_value <= num:
        el_index = i
    el_value = max(el_value, num)

el_value = list_numbers[el_index]

list_numbers[el_index] = list_numbers[-1]

list_numbers[-1] = el_value

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
