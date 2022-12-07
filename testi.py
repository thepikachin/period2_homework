class Koira:

    tehty = 0

    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        Koira.tehty = Koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")
print(f"Koiria on nyt {Koira.tehty}.")

#koira1.hauku(2)
#koira2.hauku(5)