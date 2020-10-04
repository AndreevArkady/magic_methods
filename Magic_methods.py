attributes_limit = 6

class Calculator:
    def __init__(self, init_value):
        if isinstance(init_value, Calculator):
            init_value = init_value.value
        self.__dict__['value'] = init_value
        self.__dict__['amount_of_attributes'] = 2

    def add(self, *others):
        for i in others:
            self.value += i
        return self.value

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def power(self, *args):
        powers = 1
        for x in args:
            powers *= x
        self.value **= powers
        return self

    def root(self, *args):
        exponent = 1
        for x in args:
            exponent /= x
        self.value **= exponent
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        attrs = ''
        for i in self.__dict__:
            attrs += i + ' = ' + str(self.__dict__[i]) + '; '
        return attrs

    def __add__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        self.value += value
        return self

    def __sub__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value - value)

    def __mul__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value * value)

    def __truediv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value / value)

    def __floordiv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(int(self.value // value))

    def __pow__(self, power, modulo=None):
        values = power.value if isinstance(power, Calculator) else power
        return Calculator(self.value ** values)

    def __setattr__(self, key, value):
        if self.amount_of_attributes >= attributes_limit and not hasattr(self, key):
            raise AttributeError
        if not hasattr(self, key):
            self.__dict__["amount_of_attributes"] = self.amount_of_attributes + 1
        self.__dict__[key] = value


if __name__ == '__main__':
    a = Calculator(4)
    print(a ** Calculator(2))
    # print (a.__dict__)
    print(a)
    print(6 // 2)
