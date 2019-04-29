import csv


def validate(num: str):
    print(num)
    remaining_num = (num[:15])
    print(num[0:15])


def remove_last_number(num: str):
    print(num)
    last_num = int(num[15])


remove_last_number("6447715651114770")


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")


def reverse(num: str):
    print(num)
    print(num[0:10:-1])
