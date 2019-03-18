import Special_Random


class WaterGun(object):
    def __init__(self, capacity, distance=30, stock=False):
        # These are things that a water gun has.
        # All of these should be relevant to our program.
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = 5

    def shoot(self, time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure")
            elif self.duration_of_pressure < time:
                print("You run out of pressure after firing for %s seconds" % self.duration_of_pressure)
                self.duration_of_pressure = 0
            else:
                print("You shoot for %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger!")

    def pump_it_up(self):
        self.duration_of_pressure = 5
        print("You pump the tank back to full pressure.")


# Initialize the objects
my_water_gun = WaterGun(5.2, 40, True)
your_water_gun = WaterGun(1.0, 1, False)
wiebe_water_gun = WaterGun(99999, 9999999999999, True)
kyle_water_gun = WaterGun(500)

# Do stuff with the objects
kyle_water_gun.shoot(5)
kyle_water_gun.pump_it_up()


print(Special_Random.RandomWiebe.special_random())

