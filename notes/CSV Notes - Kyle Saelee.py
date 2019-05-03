import csv


def first_num_is_four(num: str):
    first_num = int(num[0])
    if first_num == 4:
        return True
    return False


def first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False


def second_num_even(num: str):
    second_num = int(num[1])
    if second_num % 2 == 0:
        return True
    return False


def validate(num: str):
    if first_num_odd(num) and second_num_even(num):
        return True
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]  # String
            if validate(old_number):
                writer.writerow(row)
        print("OK")


def reverse(num: str):
    print(num)
    print(num[0:10:-1])


reverse("7867220926511430")


print(''.join(reversed("7867220926511430")))

# with open("Book1.csv", 'r') as old_csv:
#    reader = csv.reader(old_csv)
#   for row in reader:
#        # old_number = int(row[0]) + 1
#        old_number = row[0]
#        print(old_number)

def validate(num: str):
    reversed_version = reverse(num)
    for i in reversed_version:
        ...


