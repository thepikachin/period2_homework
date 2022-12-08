import random

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


racecars = []
for i in range(10):
    topspeed = random.randint(100, 200)
    carname = "ABC-" + str(i+1)
    car = Car(carname, topspeed)
    racecars.append(car)

raceover = False

while raceover == False:
    for car in racecars:
        if car.distancetraveled > 10000:
            raceover = True

    if raceover == False:
        for car in racecars:
            change = random.randint(-10, 15)
            car.accelerate(change)

        for car in racecars:
            car.travel(1)

print("Rekisterinumero   Huippunopeus   Tämänhetkinen nopeus   Kuljettu matka")
for car in racecars:
    print(f"{car.licensenum:17s} {car.topspeed:3d} km/h {car.currentspeed:9d} km/h {car.distancetraveled:19d} km")