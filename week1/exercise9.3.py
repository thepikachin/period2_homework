class Car:

    def __init__(self, licensenum, topspeed, currentspeed=0, distancetraveled=0):
        self.licensenum = licensenum
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.distancetraveled = distancetraveled

    def accelerate(self, speedchange):
        if self.currentspeed + speedchange < self.topspeed:
            if self.currentspeed + speedchange > 0:
                self.currentspeed = self.currentspeed + speedchange
            else:
                self.currentspeed = 0
        else:
            self.currentspeed = self.topspeed

    def travel(self, hourstraveled):
        self.distancetraveled = self.distancetraveled + (self.currentspeed * hourstraveled)


newcar = Car("ABC-123", 142, 0, 2000)
newcar.accelerate(60)
newcar.travel(1.5)
print(f"Auton rekisteritunnus: {newcar.licensenum}\nHuippunopeus: {newcar.topspeed} km/h")
print(f"Tämänhetkinen nopeus: {newcar.currentspeed} km/h\nAjettu matka: {newcar.distancetraveled} km\n")

#newcar.accelerate(30)
#newcar.accelerate(70)
#newcar.accelerate(50)
#print(f"Auton nopeus on {newcar.currentspeed} km/h.")
#newcar.accelerate(-200)
#print(f"Auton nopeus hätäjarrutuksen jälkeen on {newcar.currentspeed} km/h.")