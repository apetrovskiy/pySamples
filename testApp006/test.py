# __bases__ doesn't work! What's next?
# http://stackoverflow.com/questions/3193158/bases-doesnt-work-whats-next
class Extender(object):
    def extension(self):
        print("Some work...")

class Base(object):
    pass

Base = type('Base', (Base, Extender, object), {})
Base().extension()