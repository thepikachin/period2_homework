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

elevator1 = Elevator(1, 12)
elevator1.gotofloor(6)
elevator1.gotofloor(1)
#elevator1.gotofloor(0)
#elevator1.gotofloor(1)

