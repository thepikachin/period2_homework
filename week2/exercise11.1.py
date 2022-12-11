class Publication:

    def __init__(self, name):
        self.name = name

class Book(Publication):

    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_details(self):
        print(f"Julkaisu: {self.name}\nKirjoittaja: {self.author}\nSivumäärä: {self.pagecount}\n")

class Magazine(Publication):

    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_details(self):
        print(f"Julkaisu: {self.name}\nPäätoimittaja: {self.editor}\n")

publication1 = Magazine("Aku Ankka", "Aki Hyyppä")
publication2 = Book("Hytti n:o 6", "Rosa Liksom", 200)

publication1.print_details()
publication2.print_details()