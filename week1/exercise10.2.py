class Elevator:
    def __init__(self, bottomfloor, topfloor):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.currentfloor = self.bottomfloor

    def floorup(self):
        self.currentfloor = self.currentfloor + 1
        print(f"Hissi on nyt kerroksessa {self.currentfloor}.")

    def floordown(self):
        self.currentfloor = self.currentfloor - 1
        print(f"Hissi on nyt kerroksessa {self.currentfloor}.")

    def gotofloor(self, floorno):
        if self.bottomfloor <= floorno <= self.topfloor:
            print(f"Hissi käynnistyy. Hissi lähtee kerroksesta {self.currentfloor}.")
            if self.currentfloor < floorno:
                for i in range(self.currentfloor, floorno):
                    self.floorup()
            elif self.currentfloor > floorno:
                for i in range(floorno, self.currentfloor):
                    self.floordown()
            else:
                print(f"Hissi on jo kerroksessa {self.currentfloor}.")
        else:
            print(f"Hississä ei ole kerrosta {floorno}.")

class Building:
    def __init__(self, bottomfloor, topfloor, noofelevators):
        self.bottomfloor = bottomfloor
        self.topfloor = topfloor
        self.noofelevators = noofelevators
        self.elevatorlist = []
        for i in range(noofelevators):
            elevator = Elevator(self.bottomfloor, self.topfloor)
            self.elevatorlist.append(elevator)

    def rideelevator(self, elevatorno, floorno):
        self.elevatorlist[elevatorno].gotofloor(floorno)

#Talossa on kaksi hissiä. Huomioi että hissien numerot ovat 0 ja 1.
building1 = Building(1, 12, 2)
print(building1.elevatorlist[0].currentfloor)
print(building1.elevatorlist[1].currentfloor)
building1.rideelevator(0, 6)
building1.rideelevator(1, 12)
print(building1.elevatorlist[0].currentfloor)
print(building1.elevatorlist[1].currentfloor)
