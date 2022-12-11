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

class ElectricCar(Car):

    def __init__(self, licensenum, topspeed, batterycapacity, currentspeed=0, distancetraveled=0):
        super().__init__(licensenum, topspeed, currentspeed, distancetraveled)
        self.batterycapacity = batterycapacity

class ICEngineCar(Car):

    def __init__(self, licensenum, topspeed, tankcapacity, currentspeed=0, distancetraveled=0):
        super().__init__(licensenum, topspeed, currentspeed, distancetraveled)
        self.tankcapacity = tankcapacity

tesla = ElectricCar("ABC-15", 180, 52.5)
ford = ICEngineCar("ABC-123", 165, 32.3)

ford.accelerate(100)
tesla.accelerate(120)
ford.travel(3)
tesla.travel(3)
print("Matkamittarilukemat ovat seuraavat:")
print(f"Sähköauto: {tesla.distancetraveled} km")
print(f"Polttomoottoriauto: {ford.distancetraveled} km")
