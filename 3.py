class Cell:
    def __init__(self, n):
        self.n = n

    def make_order(self, r):
        return "\n".join(["*" * r for _ in range(self.n // r)]) + "\n" + "*" * (self.n % r)

    def __str__(self):
        return self.n

    def __add__(self, other):
        return f'Сумма  : {self.n + other.n}'

    def __sub__(self, other):
        return self.n - other.n if self.n - other.n > 0 \
            else "В первой клетке меньше ячеек или равно второй!"

    def __mul__(self, other):
        return f"Умножение : {self.n * other.n}"

    def __truediv__(self, other):
        return f"Деление : {round(self.n / other.n)}"


cell1 = Cell(190)
cell2 = Cell(130)
print(cell1 + cell2)
print(f"Раздница : {cell1 - cell2}")
print(cell1 * cell2)
print(cell1 / cell2)