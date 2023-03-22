a = -1
print(abs(a))

class Test:

    def __init__(self):
        self.a = -100

    def __abs__(self):
        self.a = -99
        return self.a

t = Test()


print(abs(t))