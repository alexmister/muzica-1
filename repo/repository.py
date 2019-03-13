
class Repository(object):
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        """
        adauga un element in lista
        :param item: noul element care trebuie adaugat
        :return: noul element adaugat
        """
        return self.__items.append(item)


    def update(self, last_item, item):
        """
        updateaza un element
        :param last_item: elementul initial, inainte de a fi updatat
        :param item: noul element care se v-a insera in lista in locul vechiului element
        :return: noul element update-at
        """
        index = self.__items.index(last_item)
        self.__items.remove(last_item)
        self.__items.insert(index, item)
        return item

    def get_all(self):
        """
        returneaza o lista cu toate elementele din lista
        :return: o lista cu toate elementele din lista
        """
        return self.__items
