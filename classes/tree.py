class Tree:
    def __init__(self, root = None):
        self.root = root
        self.weight = self.root.get_and_update_weight_recursive()

    def add_tree(self, tree):
        pass