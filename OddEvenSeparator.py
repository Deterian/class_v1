class OddEvenSeparator:
    def __init__(self):
        self.numbers = list()

    def add_number(self, a):
        self.numbers.append(a)

    def even(self):
        res = list()
        for i in self.numbers:
            if i % 2 == 0:
                res.append(i)
        return res

    def odd(self):
        res = list()
        for i in self.numbers:
            if i % 2 == 1:
                res.append(i)
        return res
