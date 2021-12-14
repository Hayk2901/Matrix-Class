class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        TODO: implement
        """
        print(self)
        print(self._matrix)
        with open('C.txt', 'w') as txt_file:
            for line in self._matrix:
                print(line)
                line = str(line)
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace(',', '')
                txt_file.write(line + "\n")

    def traspose(self):
        """
        Transpose the matrix.
        TODO: implement
        """
        new_matrix = []
        # print(self.shape)
        for i in range(self.shape[0]):
            new_matrix.append([])
            for j in range(self.shape[1]):
                new_matrix[i].append(self._matrix[j][i])
        self.read_as_list(new_matrix)
        return self

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        TODO: implement
        """
        if type(self) == type(other):
            if self.shape == other.shape:
                new_matrix = []
                for i in range(self.shape[1]):
                    new_matrix.append([])
                    for j in range(self.shape[0]):
                        new_matrix[i].append(self._matrix[i][j] + other._matrix[i][j])
                # print(new_matrix)
                self.read_as_list(new_matrix)
                return self
            else:
                raise ValueError('You can not matmul-shape error')
        else:
            raise ValueError('You can not sum-type error')

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.
        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        TODO: implement
        """
        if type(self) == type(other):
            if self.shape == other.shape:
                new_matrix = []
                for i in range(self.shape[1]):
                    new_matrix.append([])
                    for j in range(self.shape[0]):
                        new_matrix[i].append(self._matrix[i][j] * other._matrix[i][j])
                # print(new_matrix)
                self.read_as_list(new_matrix)
                return self
            else:
                raise ValueError('You can not matmul-shape error')
        else:
            raise ValueError('You can not mul-type error')

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        TODO: implement
        """
        if type(self) == type(other):
            if self.shape[0] == other.shape[1]:
                new_matrix = []
                sm = 0
                for i in range(self.shape[1]):
                    new_matrix.append([])
                    for j in range(other.shape[0]):
                        for k in range(self.shape[0]):
                            sm += self._matrix[i][k] * other._matrix[k][j]
                        new_matrix[i].append(sm)
                        sm = 0
                self.read_as_list(new_matrix)
                return self
            else:
                raise ValueError('You can not matmul-shape error')
        else:
            raise ValueError('You can not matmul-type error')

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        TODO: implement
        """
        count = 0
        if self.shape[0] == self.shape[1]:
            for i in range(self.shape[0]):
                count += self._matrix[i][i]
            return count
        else:
            raise ValueError('The Matrix has not Trace')

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """
        det = 0.0
        if self.shape[0] == self.shape[1]:
            new_matrix = self._matrix
            new_list = [new_matrix]
            while len(new_list) > 0:
                new_matrix = new_list[-1]
                new_list.pop()
                if len(new_matrix) == 2:
                    det += new_matrix[0][0] * new_matrix[1][1] - new_matrix[1][0] * new_matrix[0][1]
                else:
                    for j in range(0, len(new_matrix)):
                        new = []
                        for k in range(len(new_matrix)):
                            new.append([])
                            for l in range(len(new_matrix)):
                                new[k].append(new_matrix[k][l])
                        new.pop(0)
                        for i in range(0, len(new)):
                            new[i].pop(j)
                        if j % 2 == 1:
                            for k in range(len(new)):
                                new[k][0] *= -new_matrix[0][j]
                        if j % 2 == 0:
                            for k in range(len(new)):
                                new[k][0] *= new_matrix[0][j]
                        new_list.append(new)
            return det
        else:
            raise ValueError('You can not define determinant-shape error')
