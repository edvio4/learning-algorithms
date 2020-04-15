class UnionFind:
    array = []
    size = []

    def __init__(self, n):
        for i in range(n):
            self.array.append(i)
        self.size = [1] * n
        print(self.array)

    def get_root(self, i):
        while i != self.array[i]:
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
        return i

    def add_union(self, p, q):
        i = self.get_root(p)
        j = self.get_root(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.array[i] = j
            self.size[j] += self.size[i]
        else:
            self.array[j] = i
            self.size[i] += self.size[j]

        print(self.array)

    def is_connected(self, p, q):
        print(self.get_root(p) == self.get_root(q))
        print(self.array)


union = UnionFind(10)
union.add_union(5, 0)
union.add_union(7, 4)
union.add_union(4, 5)
union.is_connected(0, 7)
