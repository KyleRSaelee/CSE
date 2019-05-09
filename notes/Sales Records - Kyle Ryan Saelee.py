import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    for row in reader:
        region = row[0]
        country = row[1]
        item_type = row[2]
        profit = row[13]
        if item_type == "Fruits":
            print(profit)
