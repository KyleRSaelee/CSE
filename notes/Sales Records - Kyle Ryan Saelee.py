import csv


with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    clothes_profit = []
    meat_profit = []
    cosmetic_profit = []
    beverage_profit = []
    fruit_profit = []
    office_supplies_profit = []
    snacks_profit = []
    personal_care_profit = []
    household_profit = []
    vegetables_profit = []
    baby_food_profit = []
    cereal_profit = []
    for row in reader:
        item_type = row[2]
        units_sold = row[8]
        total_profit = row[13]
        if item_type == "Clothes":
            clothes_profit.append(float(total_profit))

        if item_type == "Meat":
            meat_profit.append(float(total_profit))

        if item_type == "Cosmetics":
            cosmetic_profit.append(float(total_profit))

        if item_type == "Beverages":
            beverage_profit.append(float(total_profit))

        if item_type == "Fruits":
            fruit_profit.append(float(total_profit))

        if item_type == "Office Supplies":
            office_supplies_profit.append(float(total_profit))

        if item_type == "Snacks":
            snacks_profit.append(float(total_profit))

        if item_type == "Personal Care":
            personal_care_profit.append(float(total_profit))

        if item_type == "Household":
            household_profit.append(float(total_profit))

        if item_type == "Vegetables":
            vegetables_profit.append(float(total_profit))

        if item_type == "Baby Food":
            baby_food_profit.append(float(total_profit))

        if item_type == "Cereal":
            cereal_profit.append(float(total_profit))

    print("Total profit of clothes: $%s" % sum(clothes_profit))
    print("Total profit of meats: $%s" % sum(meat_profit))
    print("Total profit of cosmetics: $%s" % sum(cosmetic_profit))
    print("Total profit of beverages: $%s" % sum(beverage_profit))
    print("Total profit of fruits: $%s" % sum(fruit_profit))
    print("Total profit of office supplies: $%s" % sum(office_supplies_profit))
    print("Total profit of snacks: $%s" % sum(snacks_profit))
    print("Total profit of personal care items: $%s" % sum(personal_care_profit))
    print("Total profit of household items: $%s" % sum(household_profit))
    print("Total profit of vegetables: $%s" % sum(vegetables_profit))
    print("Total profit of baby food: $%s" % sum(baby_food_profit))
    print("Total profit of cereal: $%s" % sum(cereal_profit))
