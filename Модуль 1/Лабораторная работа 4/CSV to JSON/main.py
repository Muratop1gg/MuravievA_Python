import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_filepath : str, json_filepath : str) -> None:
    data = []

    with open(csv_filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            data.append(i)

    with open(json_filepath, "w") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=True)




if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
