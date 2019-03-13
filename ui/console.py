class UI(object):
    def __init__(self, service):
        self.__service = service

    def add(self):
        titlu = input("Titlul melodiei: ")
        artist = input("Artistul este: ")
        gen = input("Genul este: ")
        try:
            durata = int(input("Durata este:"))
        except:
            raise ValueError("durata trebuie sa fie integru")
        self.__service.add(titlu,artist,gen,durata)

    def update(self):
        titlu = input("Titlul melodiei: ")
        artist = input("Artistul este: ")
        gen = input("Genul este: ")
        try:
            durata = int(input("Durata este:"))
        except:
            raise ValueError("durata trebuie sa fie integru")
        self.__service.update(titlu, artist, gen, durata)

    def print(self):
        melodi = self.__service.get_all()
        for music in melodi:
            print(music)

    def random(self):
        size = input("numarul de melodii de adaugat: ")
        self.__service.random(size)

    def export(self):
        pass

    def menu(self):
        print("1. Adauga melodie")
        print("2. Modificare melodie")
        print("3. Creare random")
        print("4. Exporta")

    def run(self):
        optiuni = {1:self.add, 2: self.update, 3:self.random, 4:self.export,5:self.print}
        while True:
            self.menu()
            op = int(input("optiunea este: "))
            optiuni[op]()


