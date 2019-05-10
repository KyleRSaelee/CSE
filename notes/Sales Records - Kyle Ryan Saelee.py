import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    for row in reader:
        item_type = row[2]
        units_sold = row[8]
        profit = row[13]
        if item_type == "Fruits":
            print("Total profit of fruits sold is %s. \n " % profit)
        if item_type == "Clothes":
            print("Total profit of clothes sold is %s. \n " % profit)
        if item_type == "Meat":
            print("Total profit of meat sold is %s. \n " % profit)
        if item_type == "Beverages":
