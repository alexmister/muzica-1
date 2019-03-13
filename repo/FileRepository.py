from domain.entities import Music
from repo.repository import Repository

class FileRepository(Repository):

    def __init__(self, file_name):
        Repository.__init__(self)
        self.__file_name = file_name
        self.__load_music()

    def __load_music(self):
        """
        extrage toate elementele din fisier
        :return:
        """
        self._data = []
        try:
            f = open(self.__file_name,"r")
            line = f.readline()
            line = line.strip()
            while line != "":
                arr = line.split(",")
                p = Music(arr[0], arr[1],arr[2],arr[3])
                Repository.add_item(self,p)
                line = f.readline()
                line = line.strip()
        except IOError:
            raise ValueError("Corrupted file")
        f.close()

    def __save(self):
        """
        insereza toate elementele in fisier
        :return:
        """
        f = open(self.__file_name, "w")
        Students = self.get_all()
        for s in Students:
            string = s.getTitlu() + "," + s.getArtist() + "," + s.getGen() + "," + str(s.getDurata()) + "\n"
            f.write(string)
        f.close()

    def add_item(self, item):
        """
        adauga un item in lista si in fisier
        :param item: itemul care trebuie inserat
        :return:
        """
        s = Repository.add_item(self,item)
        self.__save()
        return s


    def update(self, last_item, item):
        """
        updateaza un element
        :param last_item: elementul initial, inainte de a fi updatat
        :param item: noul element care se v-a insera in lista in locul vechiului element
        :return: noul element update-at
        """
        s = Repository.update(self,last_item, item)
        self.__save()
        return s