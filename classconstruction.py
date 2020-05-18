
class Animal():
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

class Bird():
   def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound
    
def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print animal(): required an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(),o.name(),o.sound()))

def main():
    a0 = Animal('Kitten', 'Joney', 'Meow')
    a1 = Animal('Puppy', 'Peter', 'Lol Lol')
    b0 = Bird('Peter', 'Hummy', 'Ke Ke Ke')
    print_animal(a0)
    print_animal(a1)
    print_animal(b0)
    print_animal(Animal('Monkey', 'Ranga', 'Ho Ho Ho'))

if __name__ == "__main__": main()
    