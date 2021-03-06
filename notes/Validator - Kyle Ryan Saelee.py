import csv
test_num = "4556737586899855"


def reverse(number: str):
    return number[::-1]


def remove_last_num(number: str):
    remaining_nums = number[0:15]
    print(remaining_nums)
    return True


def validate(number: str):
    last_num = int(number[15])
    remaining_nums = number[0:15]
    print(remaining_nums)
    reversed_num = list(reverse(remaining_nums))
    print(reversed_num)

    for index in range(len(reversed_num)):
        reversed_num[index] = int(reversed_num[index])


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
    writer = csv.writer(new_csv)
    print("Processing...")
    for row in reader:
        num = row[0]
        if validate(num):
            writer.writerow(row)
            print("OK")
