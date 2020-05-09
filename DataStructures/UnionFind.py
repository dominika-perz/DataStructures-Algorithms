class UnionFind:
    """
    >>> letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    >>> union_find = UnionFind(letters)
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 1, 2, 3, 4, 5, 6]
    >>> union_find.union('A', 'B')
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 2, 3, 4, 5, 6]
    >>> union_find.union('E', 'F')
    >>> print(union_find.num_components)
    5
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 2, 3, 4, 4, 6]
    >>> union_find.union('C', 'F')
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 4, 3, 4, 4, 6]
    >>> union_find.union('D', 'G')
    >>> print(union_find.num_components)
    3
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 4, 3, 4, 4, 3]
    >>> union_find.union('A', 'D')
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 4, 0, 4, 4, 3]
    >>> union_find.union('C', 'D')
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 4, 0, 0, 4, 3]
    >>> union_find.union('G', 'C')
    >>> print(union_find)
    {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    [0, 0, 0, 0, 0, 4, 0]
    >>> print(union_find.num_components)
    1
    """
    def __init__(self, items):
        self.mapping = dict(zip(items, range(len(items))))
        self.roots = list(self.mapping.values())
        self.num_components = len(self.roots)
        self.sizes = list([1]*self.num_components)

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 == root2:
            return
        elif self.sizes[root1] >= self.sizes[root2]:
            self.roots[root2] = root1
            self.sizes[root1] += self.sizes[root2]
            self.sizes[root2] = 0
        else:
            self.roots[root1] = root2
            self.sizes[root2] += self.sizes[root1]
            self.sizes[root1] = 0
        self.num_components -= 1

    def find(self, item):
        root = self.mapping[item]
        path = []
        while self.roots[root] != root:
            path.append(root)
            root = self.roots[root]
        for item in path:
            self.roots[item] = root
        return root

    def __str__(self):
        return str(self.mapping) + '\n' + str(self.roots)
