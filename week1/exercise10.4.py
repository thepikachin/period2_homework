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

class Race:

    def __init__(self, name, length, participants):
        self.name = name
        self.length = length
        self.participants = participants

    def hour_passes(self):
        for car in self.participants:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.travel(1)

    def print_standings(self):
        print("Rekisterinumero   Huippunopeus   Tämänhetkinen nopeus   Kuljettu matka")
        for car in racecars:
            print(
                f"{car.licensenum:17s} {car.topspeed:3d} km/h       {car.currentspeed:<3d} km/h               {car.distancetraveled:<5d} km")

    def race_over(self, raceover):
        for car in racecars:
            if car.distancetraveled > self.length:
                raceover = True
        return raceover

racecars = []
for i in range(10):
    topspeed = random.randint(100, 200)
    carname = "ABC-" + str(i+1)
    car = Car(carname, topspeed)
    racecars.append(car)

race = Race("Suuri romuralli", 8000, racecars)

timepassed = 0
raceover = False

while raceover == False:
    race.hour_passes()
    timepassed = timepassed + 1
    raceover = race.race_over(raceover)
    if raceover == False:
        if timepassed % 10 == 0:
            print(f"Aikaa on kulunut {timepassed} tuntia. Tämänhetkinen tilanne on:")
            race.print_standings()
    else:
        print(f"Kilpailu on päättynyt. Se kesti {timepassed} tuntia.")
        race.print_standings()
