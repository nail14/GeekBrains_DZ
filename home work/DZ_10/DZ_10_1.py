class Matrix:
    def __init__(self, kube_m):
        self.kube_m = kube_m

    def __str__(self):
        for kube in self.kube_m:
            for i in kube:
                print(f"{i:6}", end="")
            print()
        return ''
      
    def __add__(self, other):
        for i in range(len(self.kube_m)):
            for i_2 in range(len(other.kube_m[i])):
                self.kube_m[i][i_2] = self.kube_m[i][i_2] + other.kube_m[i][i_2]
        return Matrix.__str__(self)
      
m = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m.__add__(new_m))
