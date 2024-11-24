import json


def task(filepath : str) -> float:
    sum = 0
    with open(filepath) as file:
        data = json.load(file)
        for item in data:
            product = item["score"] * item["weight"]
            sum += product

    return round(sum, 3)


print(task("input.json"))
