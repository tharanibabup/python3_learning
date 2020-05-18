
class Animal():
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'Joney'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'Meow Meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound
    
    def __str__(self):
        return f'The {self.type()} is named {self.name()} and says {self.sound()}.'


def main():
    a0 = Animal(type='Kitten', name='Joney', sound='Meow')
    a1 = Animal(type='Puppy', name='Peter', sound='Lol Lol')
    b0 = Animal(type='Peter', name='Hummy', sound='Ke Ke Ke')
    print(a0)
    print(a1)
    print(b0)
    print(Animal(type='Monkey', name='Ranga', sound='Ho Ho Ho'))

if __name__ == "__main__": main()
    