class Matrix:

    def __init__(self, spisok):
        self.spisok = spisok

    def __str__(self):
        return f"{self.spisok[0][0]}    {self.spisok[0][1]}    {self.spisok[0][2]}\n{self.spisok[1][0]}" \
               f"    {self.spisok[1][1]}    {self.spisok[1][2]}\n{self.spisok[2][0]}    {self.spisok[2][1]}    {self.spisok[2][2]}"

    def __add__(self, other):
        mt3 = []
        mylist = []
        for i in range(len(self.spisok)):
            mylist = []
            for j in range(len(self.spisok[i])):
                mylist.append(self.spisok[i][j] + other.spisok[i][j])
            mt3.append(mylist)
        return Matrix(mt3)



mt1 = Matrix([[1, 5, 2], [6, 2, 7], [2, 5, 1]])
mt2 = Matrix([[5, 3, 1], [9, 1, 4], [3, 6, 2]])
print(f'{mt1}\n')
print(f'{mt2}\n')
print(mt1 + mt2)
