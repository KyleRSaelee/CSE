import csv

def validate(num: str):

    with open("SalesRecords.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
     reader = csv.reader(old_csv)
    writer = csv.writer(new_csv)
    print("Processing...")
    for row in reader:
        num = row[0]
        if validate(num):
               writer.writerow(row)
        print("OK")
