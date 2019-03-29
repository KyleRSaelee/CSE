class Room(object):
    def __init__(self, name, north=None, east=None, south=None, west=None, up=None, down=None, description="",
                 items=[], characters=[]):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.items = items
        self.characters = characters


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Weapon(Item):
    def __init__(self, name, damage_dealt, durability):
        super(Weapon, self).__init__(name, 100)
        self.damage = damage_dealt
        self.durability = durability
        self.upgrade = False


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Consumable(Item):
    def __init__(self, name, value, health_gained, health_lost, usage_amount):
        super(Consumable, self).__init__(name, value)
        self.health_gained = health_gained
        self.health_lost = health_lost
        self.usage_amount = usage_amount


class Tool(Item):
    def __init__(self, name, material):
        super(Tool, self).__init__(name, 50)
        self.material = material
        self.durability = 100


class Armor(Item):
    def __init__(self, name, material, durability):
        super(Armor, self).__init__(name, 100)
        self.material = material
        self.durability = durability
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


class PickAxe(Tool):
    def __init__(self, name, material, durability):
        super(PickAxe, self).__init__(name, material)
        self.material = material
        self.durability = durability

    def swing(self):
        self.durability -= 1
        print("You have swung your PickAxe.")


class Bow(Weapon):
    def __init__(self, name, durability):
        super(Bow, self).__init__(name, 20, durability)
        self.amount_of_arrows = 25
        self.durability = 100

    def shoot_arrow(self):
        self.amount_of_arrows -= 1
        print("You've shot an arrow.")

    def pick_up_arrow_and_reload(self):
        self.amount_of_arrows += 1
        print("You've reloaded an arrow in to your bow")


class Sword(Weapon):
    def __init__(self, name, damage_dealt, durability):
        super(Sword, self).__init__(name, damage_dealt, durability)
        self.durability = 150

    def attack(self):
        self.durability -= 5
        print("You've swung your sword.")

    def defend(self):
        self.durability -= 7
        print("You have blocked with your sword.")


class Shield(Weapon):
    def __init__(self, name, damage_dealt, durability):
        super(Shield, self).__init__(name, damage_dealt, durability)
        self.durability = 225

    def block(self):
        self.durability -= 3
        print("You have blocked with your shield.")

    def attack(self):
        self.durability -= 5
        print("You have bashed someone with your shield.")


class Axe(Weapon):
    def __init__(self, name, damage_dealt, durability):
        super(Axe, self).__init__(name, damage_dealt, durability)
        self.durability = 115

    def power_swing(self):
        self.durability -= 5
        print("You have activated power swing.")


class Spear(Weapon):
    def __init__(self, name, durability):
        super(Spear, self).__init__(name, 50, durability)
        self.durability = 200

    def throw_spear(self):
        self.durability -= 10
        print("You have threw your spear.")


class NinjaStar(Weapon):
    def __init__(self, name, durability):
        super(NinjaStar, self).__init__(name, 100, durability)
        self.durability = 250
        self.amount_of_stars = 5

    def throw_star(self):
        self.durability -= 5
        self.amount_of_stars -= 1
        print("You have threw your ninja star.")

    def pick_up_star(self):
        self.amount_of_stars += 1


class Karambit(Weapon):
    def __init__(self, name, durability):
        super(Karambit, self).__init__(name, 50, durability)
        self.durability = 500

    def slice(self):
        self.durability -= 1
        print("You have sliced your opponent.")


class Gun(Weapon):
    def __init__(self, name, damage_dealt, durability):
        super(Gun, self).__init__(name, damage_dealt, durability)
        self.name = name
        self.weapon_attachments = False


class Pistol(Gun):
    def __init__(self, name, durability):
        super(Pistol, self).__init__(name, 10, durability)
        self.durability = 250
        self.ammo = 50
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 1
        self.ammo -= 1
        print("You have shot a bullet with your pistol.")


class RampageShotgun(Gun):
    def __init__(self, name, durability):
        super(RampageShotgun, self).__init__(name, 50, durability)
        self.durability = 500
        self.ammo = 10
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 10
        self.ammo -= 10
        print("You sprayed your enemy with bullets.")


class Sniper(Gun):
    def __init__(self, name, durability):
        super(Sniper, self).__init__(name, 100, durability)
        self.durability = 1000
        self.ammo = 15
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 50
        self.durability -= 1
        print("You have shot a bullet with your sniper.")


class AssaultRifle(Gun):
    def __init__(self, name, durability):
        super(AssaultRifle, self).__init__(name, 50, durability)
        self.durability = 750
        self.ammo = 30
        self.weapon_attachments = False

    def shoot(self):
        self.durability -= 5
        self.ammo -= 1
        print("You sprayed your enemy with your Rifle.")


class Flamethrower(Gun):
    def __init__(self, name, durability):
        super(Flamethrower, self).__init__(name, 100, durability)
        self.durability = durability
        self.ammo = 1000

    def shoot(self):
        self.durability -= 10
        self.ammo -= 1
        print("You've shot flames are your opponent.")


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.damage = 10
        self.inventory = []

    def move(self, new_location):
        """This method moves a character to a new location

        self.current_location = new_location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location

    def print_inventory(self):
        for item in self.inventory:
            print(item.name)


# Armor
Trash_Helmet = Armor("Sapphire Helmet", "Garbage", 10)
Trash_ChestPlate = Armor("Sapphire ChestPlate", "Garbage", 10)
Trash_Leggings = Armor("Sapphire Leggings", "Garbage", 10)
Trash_Boots = Armor("Sapphire Boots", "Garbage", 10)
Diamond_Helmet = Armor("Diamond Helmet", "Diamond", 100)
Diamond_ChestPlate = Armor("Diamond Chestplate", "Diamond", 100)
Diamond_Leggings = Armor("Diamond Leggings", "Diamond", 100)
Diamond_Boots = Armor("Diamond Boots", "Diamond", 100)
Ancient_Helmet = Armor("Ancient Helmet", "Jewelery", 1000)
Ancient_ChestPlate = Armor("Ancient Chestplate", "Jewelery", 1000)
Ancient_Leggings = Armor("Ancient Leggings", "Jewelery", 1000)
Ancient_Boots = Armor("Ancient Boots", "Jewelery", 1000)
Hellfire_Armor = Armor("Hellfire Armor", "Unknown", 10000)

# Weapon
Steel_Sword = Sword("Steel Sword", 25, 100)
Diamond_Sword = Sword("Diamond Sword", 100, 100)
Iron_Sword = Sword("Iron Sword", 25, 50)
Ancient_Sword = Sword("Ancient Sword", 300, 500)
Battle_Axe = Axe("Battle Axe", 150, 1000)
Diamond_Axe = Axe("Diamond Axe", 100, 100)
Steel_Shield = Shield("Steel Shield", 125, 250)
spear = Weapon("Bloody Spear", 15, 100)
bow = Weapon("Ancient Bow", 30, 115)
ninja_star = Weapon("Shuriken", 75, 500)
karambit = Weapon("Marble Fade Karambit", 10000000, 1000000)
dagger = Weapon("Dagger", 1, 100)
# Tool
Diamond_PickAxe = PickAxe("Diamond Pickaxe", "Diamond", 100)
Trash_PickAxe = PickAxe("Trashy Pickaxe", "Garbage", 25)

# Gun
Shotgun = Gun("Rampage Shotgun", 20, 300)
Fire_Shotgun = Gun("Dragon Breath Shotgun", 100, 500)
pistol = Gun("Pistol", 10, 400)
sniper1 = Gun("Koshka", 150, 1000)
sniper2 = Gun("Paladin", 200, 1000)
assault_rifle = Gun("Mysterious Assault Rifle", 500, 10000)
flamethrower = Gun("Flamethrower", 100, 10000)

# Consumable
Golden_Apple = Consumable("Golden Apple", 50, 100, 0, 10)
Healing_Potion = Consumable("Healing Potion", 50, 100, 0, 1)


# Characters
Boss = Character("Boss", 1000, Shotgun, Diamond_Helmet)
Ninja = Character("Ninja", 500, ninja_star, None)
Companion = Character("Teammate", pistol, 200, None)
Ghost = Character("Ghost", 100, sniper2, Trash_ChestPlate)
Goblin = Character("Goblin", 100, dagger, None)
Soldier = Character("Soldier", 150, Fire_Shotgun, None)
Water_Monster = Character("Water Monster", 100, None, None)
Venus_Fly_Trap = Character("Venus Fly Trap", 100, bow, None)
Protector = Character("Sacred Item Protector", 1000, flamethrower, Ancient_ChestPlate)
Demon = Character("Disco Demon",  100, spear, None)
Gnome = Character("Gnome", 100, dagger, None)


DINING_ROOM = Room("Dining Room", "LIVING_ROOM", "MASTER_BEDROOM",
                   "DANCE_ROOM", "MASTER_BEDROOM", None, None, "This is the room that you are in right now. "
                                                               "There are rooms to the North, East, South and West.",
                   [], [])

MASTER_BEDROOM = Room("Master Bedroom", "BALCONY", "BATHROOM",
                      "GAME_ROOM", "MASTER_BEDROOM", None, None, "You are currently in the Master Bedroom. "
                                                                 "There is a room to the North, East, South and West.",
                      [Trash_ChestPlate], [Gnome])

LIVING_ROOM = Room("Living Room", "BACKYARD", None, "DINING_ROOM", "HALLWAY",
                   None, None, "You can travel West or South.", [Trash_Leggings],
                   [])

HALLWAY = Room("Hallway", None, "LIVING_ROOM", None,
               "GARDEN", None, None, "There is a sword on the floor, to the West is the garden.", [Trash_Boots], [])

DANCE_ROOM = Room("Dance Room", "DINING_ROOM", "SNACK_BAR", None, "FRONT_YARD", None, None, "To the west is the Front "
                                                                                            "Yard, to the East is the "
                                                                                            "Snack Bar, to the North is"
                                                                                            " the Dining Room.", [], [])

GAME_ROOM = Room("Game Room", "MASTER_BEDROOM", "POOL", "SNACK_BAR", None, None, None, "There are rooms to the East, "
                                                                                       "North and South.", [], [])

POOL = Room("Pool", None, None, None, "GAME_ROOM", None, None, "There is a room to the West.", [], [Water_Monster])

SNACK_BAR = Room("Snack Bar", "GAME_ROOM", "LIBRARY", None, "DANCE_ROOM", None, None, "There are rooms to the North, "
                                                                                      "West and South.", [flamethrower],
                 [])

BATHROOM = Room("Bathroom", None, None, None, "MASTER_BEDROOM", None, None, "There is a room to the West.", [], [])
BALCONY = Room("Balcony", None, None, "MASTER_BEDROOM", None, None, None, "There is a room to the South.", [], [])
LIBRARY = Room("Library", None, None, "RANDOM_ROOM", "SNACK_BAR", None, None, "There are rooms to the South and West.",
               [], [])

RANDOM_ROOM = Room("Random Room", None, "DINING_ROOM", None, None, None, None, "Interesting, there's a "
                                                                               "ladder here. There's also a "
                                                                               "room to the North.", [sniper2], [])

KITCHEN = Room("Kitchen", None, "DINING_ROOM", "LAUNDRY_ROOM", None, None, None, "There are rooms to the East and South"
                                                                                 "", [Golden_Apple], [])
LAUNDRY_ROOM = Room("Laundry Room", "KITCHEN", None, None, "GARAGE", None, None, "There are rooms to the North and "
                                                                                 "West.", [Healing_Potion], [])

GARAGE = Room("Garage", "STORAGE_ROOM", "LAUNDRY_ROOM", None, None, None, None, "There are rooms the North and East.")
STORAGE_ROOM = Room("Storage Room", None, None, "GARAGE", None, None, "BUNKER", "A hatch leading down to a dark room.",
                    [RampageShotgun], [])
FRONT_YARD = Room("Front Yard", None, "DANCE_ROOM", None, None, None, None, "There is a room to the East.")
ATTIC = Room("Attic", None, None, None, None, None, "LIBRARY", "You can go downstairs.", [Battle_Axe], [Protector])
BACKYARD = Room("Backyard", None, None, "LIVING_ROOM", "FOREST", None, None, "There are rooms to the South and West.")
BUNKER = Room("Bunker", None, None, "UNDERGROUND_PARKING_LOT", None, "STORAGE_ROOM", None, "You can go up or go South.",
              [Ancient_Sword], [])
FOREST = Room("Forest", None, "BACKYARD", "GARDEN", None, None, None, "You can go East or go South.", [ninja_star], [])
UNDERGROUND_PARKING_LOT = Room("Underground Parking Lot", "BUNKER", "DARK_HALLWAY", None, None, None,
                               None, "You can go North or East.", [Karambit], [Boss])


DARK_HALLWAY = Room("Dark Hallway", None, None, "ELEVATOR", "UNDERGROUND_PARKING_LOT", None, None,
                    "To the West is the Underground Parking Lot, to the South is an Elevator.", [], [Goblin])

ELEVATOR = Room("Elevator", "DARK_HALLWAY", None, None, None, "GARAGE", None, "You can go North or Up.", [spear],
                [Demon])
GARDEN = Room("Garden", "FOREST", "HALLWAY", None, None, None, None, "", [], [Venus_Fly_Trap])


# Players
player = Player(DINING_ROOM)

playing = True
directions = ['north', 'east', 'south', 'west', 'up', 'down']
# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if len(player.current_location.items) > 0:
        print("There is an item in this room.")
        pickup = input("Would you like to pick it up?")
        if pickup == "yes":
            player.inventory = player.inventory + player.current_location.items

            player.print_inventory()
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("This key does not exist.")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized.")
    if len(player.current_location.characters) > 0:
        print("There is an enemy in this room.")
