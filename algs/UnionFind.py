class WeightedQuickUnion:

    def __init__(self, n):    
        self.sz = [1]*n
        self.ind = []
        for i in range(n):
            self.ind.append(i)

    def root(self, i):
        while i != self.ind[i]:
            i = self.ind[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if p_root == q_root:
            return
        if self.sz[p_root] < self.sz[q_root]:
            self.ind[p_root] = q_root;
            self.sz[q_root] += self.sz[p_root]
        else:
            self.ind[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]


class QuickUnionPC1:

    def __init__(self, n):    
        self.ind = []
        for i in range(n):
            self.ind.append(i)

    def root(self, i):
        self.ind[i] = self.ind[self.ind[i]]
        while i != self.ind[i]:
            i = self.ind[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        self.ind[q_root] = p_root
