#coding:utf-8

class Node:
    def __init__ (self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST_Tree:
    def __init__ (self, node_list):
        self.root = None
        for data in node_list:
            self.insert(data)

    # 搜索
    def search (self, node, parent, data):
        if node is None:
            return False, parent
        if node.data == data:
            return True, node
        if node.data > data:
            return self.search(node.left_child, node, data)
        if node.data < data:
            return self.search(node.right_child, node, data)

    # 插入
    def insert (self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            flag, n = self.search(self.root, self.root, data)
            if not flag:
                new_node = Node(data)
                if data > n.data:
                    n.right_child = new_node
                else:
                    n.left_child = new_node

    def delete (self, node, data):
        flag, n = self.search(node, node, data)
        if flag is False:
            print('delete fall')
        else:
            if n.left_child is None:
                p = n.right_child
                n.data = p.data
                n.right_child = p.right_child
                n.left_child = p.left_child
                del p
            elif n.right_child is None:
                p = n.left_child
                n.data = p.data
                n.right_child = p.right_child
                n.left_child = p.left_child
                del p
            else:
                r_p = n.right_child
                if r_p.left_child is None:
                    n.data = r_p.data
                    n.right_child = r_p.right_child
                    del r_p
                else:
                    p = r_p.left_child
                    while p.left_child is not None:
                        r_p = p
                        p = p.left_child
                    n.data = p.data
                    r_p.left_child = p.right_child
                    del p

    def pre_order_traverse (self, node):
        if node is not None:
            print(node.data)
            self.pre_order_traverse(node.left_child)
            self.pre_order_traverse(node.right_child)

    def in_order_traverse (self, node):
        if node is not None:
            self.in_order_traverse(node.left_child)
            print(node.data)
            self.in_order_traverse(node.right_child)

    def post_order_traverse (self, node):
        if node is not None:
            self.post_order_traverse(node.left_child)
            self.post_order_traverse(node.right_child)
            print(node.data)


if __name__ == '__main__':
    a = [49, 13, 87, 55,74, 25, 71, 39, 21]
    bst = BST_Tree(a)
    bst.in_order_traverse(bst.root)
    bst.insert(59)
    print('after')
    bst.in_order_traverse(bst.root)
    bst.delete(bst.root, 25)
    print('then')
    bst.in_order_traverse(bst.root)
    bst.delete(bst.root, 1)
