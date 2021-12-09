class Point:

    def __init__(self, value):
        self.value = value
        self.mark = False

    def __str__(self):
        return f"value: {self.value}, marked: {self.mark}"

    def get_value(self):
        return self.value

    def get_mark(self):
        return self.mark

    def mark_point(self):
        self.mark = True
