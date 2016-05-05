class Base():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print("id = %d, name = %s" % (self.id, self.name))

