class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str("\n".join(["\t".join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        spis = []
        n = []
        try:
            for i in range(len(self.args)):
                for i2 in range(len(self.args[i])):
                    if len(self.args[i]) == len(other.args[i]):
                        n.append(self.args[i][i2] + other.args[i][i2])

                    else:
                        return "Матрицы разных размеров!"
                spis.append(n)
                n = []
        except IndexError:
            print("Матрицы разных размеров!")
        return "\n".join(map(str, spis))


matrix1 = Matrix([[2,4],[3,1],[0,4]])
matrix2 = Matrix([[0,2],[2,2],[1,3]])

print(matrix1+matrix2)