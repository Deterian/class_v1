class Button:
    def __init__(self):
        self.count = 0

    def click(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def click_count(self):
        print(self.count)
