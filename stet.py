class FooBar:
    def __init__(self, value=42):
        self.somevar = value


f = FooBar()
print(f.somevar)

class A:
    def hello(self):
        print("Hello, i'm A.")


class B(A):
    def hello(self):
        print("Hello, i'm B.")


a = A()
b = B()

a.hello()
b.hello()


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah....')
            self.hungry = False
        else:
            print('No, thranks!')


b = Bird()
b.eat()
b.eat()


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()


def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, item):
        check_index(item)

        try:
            return self.changed[item]
        except KeyError:
            return self.start + item * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)
print(s[4])
s[4] = 2
print(s[4])
print(s[5])


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1
        return super(CounterList, self).__getitem__(item)


cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[3:6]
print(cl)
print(cl.counter)
print(cl[4] + cl[2])
print(cl.counter)


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size())
r.size = 150, 100
print(r.width)


class MyClass:

    @staticmethod
    def smeth():
        print('this is astatic method')

    @classmethod
    def cmeth(cls):
        print('this is class method of', cls)


MyClass.smeth()
MyClass.cmeth()


class Rectangles:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, item):
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()


res = Rectangle()

res.size = (100, 50)
print(res.size)


class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()

for f in fibs:
    if f > 1000:
        print(f)
        break


it = iter([1, 2, 3])

print(next(it))

print(next(it))


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


nested = [[1, 2], [3, 4], [5]]

print(list(flatten(nested)))


def flattens(nested):
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flattens(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flattens([[[1], 2], 3, 4, [5, [6, 7]], 8, 'sdfas'])))
