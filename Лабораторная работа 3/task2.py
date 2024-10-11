def find_common_participants(group1: str, group2: str, separator : str = ","):
    group1 = group1.split(separator)
    group2 = group2.split(separator)

    res = []

    for i in group1:
        if group2.count(i):
            res.append(i)

    return sorted(res)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
