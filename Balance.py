class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, r):
        self.right = r

    def add_left(self, u):
        self.left = u

    def result(self):
        if self.left > self.right:
            print('L')
        if self.left < self.right:
            print('R')
        else:
            print('=')
