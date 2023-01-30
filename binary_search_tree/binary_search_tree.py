class _Node:
    __slots__ = '_element', '_left', '_right'
    def __init__(self, element , left = None, right = None):
        self._element = element
        self._left = left
        self._right = right

class binarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                return 
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n
    
    def search(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right

        if not p:
            return False

        if p._left and p._right:
            s = p._left
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps

        c = None
        if p._left:
            c = p._left
        else:
            c = p._right

        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c

        


    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end = ' ')
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end = ' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end = ' ')

    def levelorder(self, troot):
        Q = []
        t = troot
        print(t._element, end = ' ')
        Q.append(t)
        while Q:
            t = Q.pop(0)
            if t._left:
                print(t._left._element, end = ' ')
                Q.append(t._left)
            if t._right:
                print(t._right._element, end = ' ')
                Q.append(t._right)


B = binarySearchTree()
B.insert(B._root, 50)
B.insert(B._root, 30)
B.insert(B._root, 80)
B.insert(B._root, 10)
B.insert(B._root, 40)
B.insert(B._root, 60)
B.insert(B._root, 90)
B.insert(B._root, 10) # Binary search doesn't support duplicate. 
B.insert(B._root, 5)
print("Inorder treaversal")
B.inorder(B._root)
print()
print("preorder treaversal")
B.preorder(B._root)
print()
print("postorder treaversal")
B.postorder(B._root)
print()
print("levelorder treaversal")
B.levelorder(B._root)
print()
print(B.search(40))
print(B.search(100))
B.delete(10)
print("Inorder traversal")
B.inorder(B._root)