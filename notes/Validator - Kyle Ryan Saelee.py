import csv


def remove_last_num(num: str):
    print(num)
    remaining_nums = num[0:15]
    print(remaining_nums)


def reverse(num: str):
    print(num)
    return num[::-1]


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            credit_card_num = row[0]
            remove_last_num(credit_card_num)


def validate(num: str):
    reversed_version = reverse(num)
    for i in reversed_version:
        return True


remove_last_num("8721389808186650")
reverse("872138980818665")
