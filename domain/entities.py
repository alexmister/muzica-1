class Music(object):
    def __init__(self,titlu,artist,gen,durata):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    def getTitlu(self):
        return self.__titlu

    def getGen(self):
        return self.__gen

    def getDurata(self):
        return self.__durata

    def getArtist(self):
        return self.__artist

    def setArtist(self, newArtist):
        self.__artist = newArtist

    def setGen(self, newGen):
        self.__gen = newGen

    def setDurata(self, newDuarata):
        self.__durata = newDuarata

    def __str__(self):
        return self.__titlu + " " + self.__artist + " " + self.__gen + " " + str(self.__durata)