from math import gcd

class RationalFraction:
    def __init__(self, num, denom=1):
        self.num = num
        if denom == 0:
            print("Деление на 0 невозможно! Знаминатель заменён на 1")
            self.denom = 1
        else:
            self.denom = denom
        self.simplify()

    def simplify(self):
        fr_gcd = gcd(self.num, self.denom)
        self.num //= fr_gcd
        self.denom //= fr_gcd
        if self.denom < 0:
            self.num = -self.num
            self.denom = -self.denom

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __sub__(self, other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom
        return RationalFraction(new_num, new_denom)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Деление на ноль невозможно.")
        new_num = self.num * other.denom
        new_denom = self.denom * other.num
        return RationalFraction(new_num, new_denom)

    def __pow__(self, exponent):
        new_num = self.num ** exponent
        new_denom = self.denom ** exponent
        return RationalFraction(new_num, new_denom)

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def fr_add_int(self, integ):
        fr2 = RationalFraction(integ, 1)
        return self + fr2