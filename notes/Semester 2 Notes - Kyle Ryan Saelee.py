print("Hello World")
# This is a single-line comment
cars = 5
driving = True

print("I have %s cars" % cars)
print("I have " + str(cars) + " cars")

age = input("How old are you?")
print("Wow are you really %s years old!" % age)

colors_list = ["purple", "blue", "orange", "yellow", "red"]
colors_list.append("green")
print(colors_list)

colors_list.pop(0)
print(colors_list)

if item_type == "Fruits":
    print("Total profit of fruits sold is %s. \n " % profit)

if item_type == "Meat":
    print("Total profit of meat sold is %s. \n " % profit)
if item_type == "Beverages":
    print()


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("processing")
    sum_profit = {}
    for row in reader:
        if row[0] == "Region":
            continue
        item_sold = row[2]
        total_profit = round(float(row[13]), 2)
        if item_sold not in sum_profit:
            sum_profit[item_sold] = total_profit
        else:
            sum_profit[item_sold] += total_profit

    print(sum_profit)
    print("The item that made the highest profit was: %s" %
          (max(sum_profit, key=sum_profit.get) + " with a total of $" + str(max(sum_profit.values()))))



