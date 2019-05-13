import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    sum_profit = []
    for row in reader:
        item_type = row[2]
        units_sold = row[8]
        total_profit = row[13]
        if item_type == "Clothes":
            sum_profit.append(float(total_profit))
    print(sum(sum_profit))
