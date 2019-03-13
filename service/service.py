
from repo.FileRepository import FileRepository
from domain.entities import Music
import random
import string

class MusicService(object):
    def __init__(self, repository):
        self.__repository = repository
        self.__genuri = ['Rock', 'Pop', 'Jazz', 'Alele']

    def get_all(self):
        """
        returnam toate elementele din lista
        :return: returnam toate elementele din lista
        """
        return self.__repository.get_all()

    def add(self, titlu, artist, gen, durata):
        """
        creeaza o noua entitate de tipul muzica
        :param titlu: titlul piesei
        :param artist: artistul piesei
        :param gen: genul piesei
        :param durata: durata piesei
        :return:
        """
        if gen in self.__genuri:
            music = Music(titlu, artist, gen, durata)
            self.__repository.add_item(music)
            return music
        return ValueError

    def update(self, titlu, artist, gen, durata):
        """
            updateaza o noua entitate de tipul muzica
            :param titlu: titlul piesei
            :param artist: artistul piesei
            :param gen: genul piesei
            :param durata: durata piesei
            :return:
        """
        if gen in self.__genuri:
            music = self.get_all()
            for melodie in music:
                if titlu == melodie.getTitlu() and artist == melodie.getArtist():
                    music = Music(titlu, artist, gen, durata)
                    self.__repository.update(melodie,music)
            return music
        return ValueError

    def save(self):
        """
        salveaza toate datele in fisier si in memorie
        :return:
        """
        music = self.get_all()
        save = FileRepository('data/data')
        for melodie in music:
            save.add_item(melodie)

    def random(self, size):
        """
        genereaza un anumit numar de elemente radom
        :param size: numarul de elemente de adaugat
        :return:
        """
        for i in range(int(size)):
            gen = random.sample(['Jazz', 'Pop', 'Rock', 'Altele'], k=1)
            durata = random.sample(range(1,300),k=1)

            gen1 = ''
            for i in gen:
                gen1=i
            print(gen1)
            durata1 = ''
            for i in durata:
                durata1 = i
            print(durata1)
            first1 = rest1 = ''
            for i in range(2):
                first = str(random.choices(string.ascii_lowercase))
                vocal = str(random.sample(['a','e','i','o','u'],k=1))
                first1 = first1 + first + vocal
            for i in range(3):
                rest = random.choices(string.ascii_lowercase)
                vocal = random.sample(['a', 'e', 'i', 'o', 'u'], k=1)
                rest1 = rest1 + str(rest) + str(vocal)
            first=rest = ''
            for i in first1:
                if i in string.ascii_lowercase:
                    first = first+i
            for i in rest1:
                if i in string.ascii_lowercase:
                    rest = rest+i
            titlu = str(first) +" " + rest
            print(titlu)
            first1 = rest1 = ''
            for i in range(2):
                first = str(random.choices(string.ascii_lowercase))
                vocal = str(random.sample(['a', 'e', 'i', 'o', 'u'], k=1))
                first1 = first1 + first + vocal
            for i in range(3):
                rest = random.choices(string.ascii_lowercase)
                vocal = random.sample(['a', 'e', 'i', 'o', 'u'], k=1)
                rest1 = rest1 + str(rest) + str(vocal)
            first = rest = ''
            for i in first1:
                if i in string.ascii_lowercase:
                    first = first + i
            for i in rest1:
                if i in string.ascii_lowercase:
                    rest = rest + i
            artist = str(first) + " " + rest
            print(artist)
            music = Music(titlu, artist, gen1, durata1)
            self.__repository.add_item(music)

