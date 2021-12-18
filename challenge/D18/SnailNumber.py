class SnailNumber:
    def __init__(self, **kwargs):
        self.data = {}
        self.data.update(kwargs)

    @classmethod
    def from_int(cls, i):
        return cls(**{"":i})

    def combine(self, other):
        res = {}
        for k,v in self.data.items():
            res["l" + k] = v
        for k,v in other.data.items():
            res["r" + k] = v
        return SnailNumber(**res)

    def __add__(self, other):
        return self.combine(other).explode_and_split_all()

    @classmethod
    def subparse(cls, v):
        if isinstance(v, list):
            return cls.subparse(v[0]).combine(cls.subparse(v[1]))
        else:
            return cls.from_int(v)

    @classmethod
    def parse(cls, v):
        return cls.subparse(v).explode_and_split_all()

    def bra(self):
        res = {}
        for k,v in self.data.items():
            if k.startswith("l"):
                res[k[1:]] = v
        return SnailNumber(**res)

    def ket(self):
        res = {}
        for k,v in self.data.items():
            if k.startswith("r"):
                res[k[1:]] = v
        return SnailNumber(**res)

    def expand(self):
        if "" in self.data:
            return self.data[""]
        else:
            return [self.bra().expand(), self.ket().expand()]

    def __str__(self):
        return str(self.expand())

    def __repr__(self):
        return str(self.data)

    def can_explode(self):
        return any(len(x) >= 5 for x in self.data)

    def order(self):
        return sorted(list(self.data.keys()))

    def regular_left(self, key):
        i = self.order().index(key)
        if i > 0:
            return self.order()[i-1]

    def regular_right(self, key):
        i = self.order().index(key)
        if i < len(self.order()) - 1:
            return self.order()[i+1]

    def explode(self):
        assert self.can_explode()

        #print(self.order())

        left = next(x for x in self.order() if len(x) >= 5)


        #print(left)

        right = left[:-1] + "r"
        base = left[:-1]

        reg_left = self.regular_left(left)
        reg_right = self.regular_right(right)

        if reg_left is not None:
            self.data[reg_left] += self.data[left]

        if reg_right is not None:
            self.data[reg_right] += self.data[right]

        del self.data[left]
        del self.data[right]
        self.data[base] = 0
        #print('res', repr(self))
        #print('res', self)

    def explode_and_split_all(self):
        while self.can_explode() or self.can_split():
            if self.can_explode():
                self.explode()
            else:
                self.split()
        return self

    def can_split(self):
        return any(v > 9 for v in self.data.values())

    def split(self):
        for k in self.order():
            v = self.data[k]
            if v > 9:
                break
        else:
            assert False, "no break"

        left = k + "l"
        right = k + "r"

        del self.data[k]

        self.data[left] = v//2
        self.data[right] = v - (v//2)

    def magnitude(self):
        if "" in self.data:
            return self.data[""]
        else:
            return 3*self.bra().magnitude() + 2*self.ket().magnitude()
