import numpy as np

class Node:
    def _init_(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

class KDTree:
    def _init_(self, points):
        self.k = points.shape[1]
        self.root = self.build_kdtree(points)

    def build_kdtree(self, points, depth=0):
        n = points.shape[0]
        if n <= 0:
            return None
        axis = depth % self.k
        sorted_points = points[points[:, axis].argsort()]
        mid = n // 2
        return Node(sorted_points[mid], axis,
                    self.build_kdtree(sorted_points[:mid], depth + 1),
                    self.build_kdtree(sorted_points[mid + 1:], depth + 1))

    def insert(self, point):
        def _insert(root, point, depth=0):
            if root is None:
                return Node(point, depth % self.k)
            axis = root.axis
            if point[axis] < root.point[axis]:
                root.left = _insert(root.left, point, depth + 1)
            else:
                root.right = _insert(root.right, point, depth + 1)
            return root
        self.root = _insert(self.root, point)

    def print_kdtree(self, root, level=0):
        if root is not None:
            print("  " * level, root.point)
            self.print_kdtree(root.left, level + 1)
            self.print_kdtree(root.right, level + 1)

points = np.array([[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]])
tree = KDTree(points)
print("Initial tree:")
tree.print_kdtree(tree.root)

tree.insert(np.array([3,5]))
print("After insertion of point (3,5):")
tree.print_kdtree(tree.root)