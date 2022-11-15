class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if self.number != other.number:
            return abs(self.number - other.number)
        else:
            return "Клетки имеют одинаковый размер"

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number // other.number

    def make_order(self, row):
        str = ""
        for i in range(self.number//row):
            for j in range(row):
                str += "*"
            str += "\n"
        for i in range(self.number % row):
            str         += "*"
        return str
        # for i in range(self.number//row):
        #     for j in range(row):
        #         print("*", end='')
        #     print("")
        # for i in range(self.number % row):
        #     print("*", end='')
c1 = Cell(18)
c2 = Cell(15)
print(c1 * c2)
print(c1.make_order(5))