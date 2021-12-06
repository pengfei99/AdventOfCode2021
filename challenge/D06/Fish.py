class Fish:
    def __init__(self, counter):
        self.counter = counter
        self.can_make_fish = False

    def pass_day(self):
        if self.counter == 0:
            self.can_make_fish = True
        else:
            self.counter = self.counter - 1

    def make_fish(self):
        self.counter = 6
        self.can_make_fish=False
        return Fish(8)

    def ready_to_make_fish(self):
        return self.can_make_fish

    def __str__(self):
        return f"fish counter:{self.counter}, can_make_fish:{self.can_make_fish}"



