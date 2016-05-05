from base import Base


class Child(Base):
    def __init__(self, id, name):
        # super().id = id
        # super().name = name
        super().__init__(id, name)

    def show(self):
        print("id = %d, name = %s" % (self.id, self.name))
        print(self.__class__)
        print(self.__dict__)
        print(self.__dir__())
        print(self.__doc__)
        print(self.__module__)