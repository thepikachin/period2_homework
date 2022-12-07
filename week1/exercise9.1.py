class Car:

    def __init__(self, licensenum, topspeed, currentspeed=0, distancetraveled=0):
        self.licensenum = licensenum
        self.topspeed = topspeed
        self.currentspeed = currentspeed
        self.distancetraveled = distancetraveled


newcar = Car("ABC-123", 142)
print(f"Auton rekisteritunnus: {newcar.licensenum}\nHuippunopeus: {newcar.topspeed} km/h")
print(f"Tämänhetkinen nopeus: {newcar.currentspeed} km/h\nAjettu matka: {newcar.distancetraveled} km")