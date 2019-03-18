class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Armor(Item):
    def __init__(self, name, material, value=100):
        super(Armor, self).__init__(name, value)
        self.material = material
        self.durability = 100
        self.equipped = False


class Helmet(Armor):
    def __init__(self, name, material):
        super(Helmet, self).__init__(name, material, 25)

    def equip(self):
        self.equipped = True
        print("You have equipped your helmet.")

    def un_equip(self):
        self.equipped = False
        print("You have unequipped your helmet.")


class ChestPlate(Armor):
    def __init__(self, name, material):
        super(ChestPlate, self).__init__(name, material, 50)

    def equip(self):
        self.equipped = True
        print("You have equipped your ChestPlate.")

    def un_equip(self):
        self.equipped = False
        print("You have unequipped your ChestPlate.")


class Leggings(Armor):
    def __init__(self, name, material):
        super(Leggings, self).__init__(name, material, 25)

    def equip(self):
        self.equipped = True
        print("You have equipped your leggings")

    def un_equip(self):
        self.equipped = False
        print("You have unequipped your leggings.")


class Boots(Armor):
    def __init__(self, name, material):
        super(Boots, self).__init__(name, material, 25)

    def equip(self):
        self.equipped = True
        print("You have equipped your boots.")

    def un_equip(self):
        self.equipped = False
        print("You have unequipped your boots.")


class Tool(Item):
    def __init__(self, name, material):
        super(Tool, self).__init__(name, 50)
        self.material = material
        self.durability = 100


class PickAxe(Tool):
    def __init__(self, name, material):
        super(PickAxe, self).__init__(name, material)
        self.material = material

    def swing(self):
        self.durability -= 1
        print("You have swung your PickAxe.")


class Weapon(Item):
    def __init__(self, name, material, damage_dealt):
        super(Weapon, self).__init__(name, 100)
        self.material = material
        self.damage = damage_dealt
        self.durability = 100
        self.upgrade = False


class Bow(Weapon):
    def __init__(self, name, material):
        super(Bow, self).__init__(name, material, 20)
        self.amount_of_arrows = 25

    def shoot_arrow(self):
        self.amount_of_arrows -= 1
        print("You've shot an arrow.")

    def pick_up_arrow_and_reload(self):
        self.amount_of_arrows += 1
        print("You've reloaded an arrow in to your bow")


class Sword(Weapon):
    def __init__(self, name, material, damage_dealt):
        super(Sword, self).__init__(name, material, damage_dealt)
        self.durability = 150

    def attack(self):
        self.durability -= 5
        print("You've swung your sword.")

    def defend(self):
        self.durability -= 7
        print("You have blocked with your sword.")


Ancient_Sword = Sword("Ancient Sword", "Jewelery", 300)


class Shield(Weapon):
    def __init__(self, name, material, damage_dealt):
        super(Shield, self).__init__(name, material, damage_dealt)
        self.durability = 225

    def block(self):
        self.durability -= 3
        print("You have blocked with your shield.")

    def attack(self):
        self.durability -= 5
        print("You have bashed someone with your shield.")


Steel_Shield = Shield("Steel Shield", "Steel", 125)


class Axe(Weapon):
    def __init__(self, name, material, damage_dealt):
        super(Axe, self).__init__(name, material, damage_dealt)
        self.durability = 115

    def power_swing(self):
        self.durability -= 5
        print("You have activated power swing.")


Diamond_Axe = Axe("Diamond Axe", "Diamond", 100)


class Spear(Weapon):
    def __init__(self, name, material):
        super(Spear, self).__init__(name, material, 50)
        self.durability = 200

    def throw_spear(self):
        self.durability -= 10
        print("You have threw your spear.")


class NinjaStar(Weapon):
    def __init__(self, name, material):
        super(NinjaStar, self).__init__(name, material, 100)
        self.durability = 250
        self.amount_of_stars = 5

    def throw_star(self):
        self.durability -= 5
        self.amount_of_stars -= 1
        print("You have threw your ninja star.")

    def pick_up_star(self):
        self.amount_of_stars += 1


class Karambit(Weapon):
    def __init__(self, name, material):
        super(Karambit, self).__init__(name, material, 50)
        self.durability = 500

    def slice(self):
        self.durability -= 1
        print("You have sliced your opponent.")


class Pistol(Weapon):
    def __init__(self, name, material):
        super(Pistol, self).__init__(name, material, 10)
        self.durability = 250
        self.ammo = 50
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 1
        self.ammo -= 1
        print("You have shot a bullet with your pistol.")


class RampageShotgun(Weapon):
    def __init__(self, name, material):
        super(RampageShotgun, self).__init__(name, material, 50)
        self.automatic = False
        self.durability = 500
        self.ammo = 10
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 10
        self.ammo -= 10
        self.automatic = True
        print("You sprayed your enemy with bullets.")


class Sniper(Weapon):
    def __init__(self, name, material):
        super(Sniper, self).__init__(name, material, 100)
        self.durability = 1000
        self.ammo = 15
        self.weapon_attachments = False
        self.automatic = False

    def shoot(self):
        self.automatic = False
        self.durability -= 50
        self.durability -= 1
        print("You have shot a bullet with your sniper.")


class AssaultRifle(Weapon):
    def __init__(self, name, material):
        super(AssaultRifle, self).__init__(name, material, 50)
        self.durability = 750
        self.ammo = 30
        self.weapon_attachments = False
        self.automatic = False

    def shoot(self):
        self.durability -= 5
        self.ammo -= 1
        self.automatic = True
        print("You sprayed your enemy with your Rifle.")


class RocketLauncher(Weapon):
    def __init__(self, name, material):
        super(RocketLauncher, self).__init__(name, material, 200)
        self.durability = 250
        self.ammo = 5
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 10
        self.ammo -= 1
        print("You have launched a rocket at your opponent.")


class Consumable(Item):
    def __init__(self, name, value, health_gained, health_lost, usage_amount):
        super(Consumable, self).__init__(name, value)
        self.health_gained = health_gained
        self.health_lost = health_lost
        self.usage_amount = usage_amount


class HealingPotion(Consumable):
    def __init__(self, name, value, health_gained, health_lost, usage_amount):
        super(HealingPotion, self).__init__(name, value, health_gained, health_lost, usage_amount)
        self.health_gained = 100
        self.health_lost = 0
        self.usage_amount = 1

    def drink(self):
        self.health_gained += 100
        self.usage_amount -= 1
        print("You drank a healing potion.")


Golden_Apple = Consumable("Golden Apple", 50, 100, 0, 10)


class Valuables(Item):
    def __init__(self, name, value, rarity):
        super(Valuables, self).__init__(name, value)
        self.name = name
        self.value = value
        self.rarity = rarity
