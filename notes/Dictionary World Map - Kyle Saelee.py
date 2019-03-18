world_map = {
    "DINING_ROOM": {
        "NAME": "Dining Room",
        "DESCRIPTION": "This is the room that you are in right now. There are rooms to the"
                       " North, East, South, and West.",
        "PATHS": {
            "NORTH": "LIVING_ROOM",
            "SOUTH": "DANCE_ROOM",
            "EAST": "MASTER_BEDROOM",
            "WEST": "KITCHEN"
        }
    },
    "MASTER_BEDROOM": {
        "NAME": "Master Bedroom",
        "DESCRIPTION": "You are currently in the Master Bedroom. You see that there is a suitcase on the bed."
                       "There is a room to the North, East, South and West.",
        "PATHS": {
            "EAST": "BATHROOM",
            "SOUTH": "GAME_ROOM",
            "NORTH": "BALCONY",
            "WEST": "MASTER_BEDROOM"
        }
    },
    "LIVING_ROOM": {
        "NAME": "Living Room",
        "DESCRIPTION": "There are many boxes in here, you can go West or South.",

        "PATHS": {
            "SOUTH": "DINING_ROOM",
            "WEST": "HALLWAY",
            "NORTH": "BACKYARD"
        }
    },
    "HALLWAY": {
        "NAME": "Hallway",
        "DESCRIPTION": "There is a sword on the floor, to the West is the garden. To the east is the Living Room",
    
        "PATHS": {
            "WEST": "GARDEN",
            "EAST": "LIVING_ROOM"
        }
    },
    "GARDEN": {
        "NAME": "Garden",
        "DESCRIPTION": "This room is filled with dead flowers and plants. It looks like they haven't been"
                       " watered in years. To the east is the hallway and to the north is the forest.",

        "PATHS": {
            "EAST": "HALLWAY",
            "NORTH": "FOREST"
        }
    },
    "DANCE_ROOM": {
        "NAME": "Dance Room",
        "DESCRIPTION": "To the west is the front yard, to the east is the snack bar, to the north is the dining room.",

        "PATHS": {
            "WEST": "FRONT_YARD",
            "EAST": "SNACK_BAR",
            "NORTH": "DINING_ROOM"
        }
    },
    "GAME_ROOM": {
        "NAME": "Game Room",
        "DESCRIPTION": "There are rooms to the East, North and South.",

        "PATHS": {
            "EAST": "POOL",
            "NORTH": "MASTER_BEDROOM",
            "SOUTH": "SNACK_BAR"
        }
    },
    "POOL": {
        "NAME": "Pool",
        "DESCRIPTION": "There is a room to the West.",

        "PATHS": {
            "WEST": "GAME_ROOM"
        }
    },
    "SNACK_BAR": {
        "NAME": "Snack Bar",
        "DESCRIPTION": "There are rooms to the North, West, and East.",

        "PATHS": {
            "NORTH": "GAME_ROOM",
            "WEST": "DANCE_ROOM",
            "EAST": "LIBRARY"
        }
    },
    "BATHROOM": {
        "NAME": "Bathroom",
        "DESCRIPTION": "There's a room to the West.",

        "PATHS": {
            "WEST": "MASTER_BEDROOM"
        }
    },
    "BALCONY": {
        "NAME": "Balcony",
        "DESCRIPTION": "There is a room to the South.",

        "PATHS": {
            "SOUTH": "MASTER_BEDROOM"
        }
    },
    "LIBRARY": {
        "NAME": "Library",
        "DESCRIPTION": "There are rooms to the South and West.",

        "PATHS": {
            "SOUTH": "RANDOM_ROOM",
            "WEST": "SNACK_BAR"
        }
    },
    "RANDOM_ROOM": {
        "NAME": "Random Room",
        "DESCRIPTION": "Interesting, there's a ladder in here. There's also a room to the North.",

        "PATHS": {
            "NORTH": "LIBRARY",
            "UP": "ATTIC"
        }
    },
    "KITCHEN": {
        "NAME": "Kitchen",
        "DESCRIPTION": "There are rooms to the East and South",

        "PATHS": {
            "EAST": "DINING_ROOM",
            "SOUTH": "LAUNDRY_ROOM"
        }
    },
    "LAUNDRY_ROOM": {
        "NAME": "Laundry Room",
        "DESCRIPTION": "There are rooms to the North and the West.",

        "PATHS": {
            "NORTH": "KITCHEN",
            "WEST": "GARAGE"
        }
    },
    "GARAGE": {
        "NAME": "Garage",
        "DESCRIPTION": "There are rooms to the North and the East.",

        "PATHS": {
            "NORTH": "STORAGE_ROOM",
            "EAST": "LAUNDRY_ROOM"
        }
    },
    "STORAGE_ROOM": {
        "NAME": "Storage Room",
        "DESCRIPTION": "A hatch leading down to a dark room.",

        "PATHS": {
            "SOUTH": "GARAGE",
            "DOWN": "BUNKER"
        }
    },
    "FRONT_YARD": {
        "NAME": "Front Yard",
        "DESCRIPTION": "There is a room to the East.",

        "PATHS": {
            "EAST": "DANCE_ROOM"
        }
    },
    "ATTIC": {
        "NAME": "Attic",
        "DESCRIPTION": "You can go downstairs.",

        "PATHS": {
            "DOWN": "LIBRARY"
        }
    },
    "BACKYARD": {
        "NAME": "Backyard",
        "DESCRIPTION": "There are rooms to the South and West.",

        "PATHS": {
            "SOUTH": "LIVING_ROOM",
            "WEST": "FOREST"
        }
    },
    "BUNKER": {
        "NAME": "Bunker",
        "DESCRIPTION": "You can go up or go South.",

        "PATHS": {
            "UP": "STORAGE_ROOM",
            "SOUTH": "UNDERGROUND_PARKING_LOT"
        }
    },
    "FOREST": {
        "NAME": "Forest",
        "DESCRIPTION": "You can go East or go South.",

        "PATHS": {
            "EAST": "BACKYARD",
            "SOUTH": "GARDEN"
        }
    },
    "UNDERGROUND_PARKING_LOT": {
        "NAME": "Underground Parking Lot",
        "DESCRIPTION": "You can travel North or go East.",

        "PATHS": {
            "NORTH": "BUNKER",
            "EAST": "DARK_HALLWAY"
        }
    },
    "DARK_HALLWAY": {
        "NAME": "Dark Hallway",
        "DESCRIPTION": "To the West is the underground parking lot, to the south is an elevator.",

        "PATHS": {
            "WEST": "UNDERGROUND_PARKING_LOT",
            "SOUTH": "ELEVATOR"
        }
    },
    "ELEVATOR": {
        "NAME": "Elevator",
        "DESCRIPTION": "You can go North or Up.",

        "PATHS": {
            "NORTH": "DARK_HALLWAY",
            "UP": "GARAGE"
        }
    },

}
# Other Variables
currrent_node = world_map["DINING_ROOM"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    print(currrent_node["NAME"])
    print(currrent_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ["q", "quit", "exit"]:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = currrent_node["PATHS"][command.upper()]
            currrent_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized.")
