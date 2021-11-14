import random
import string
node_per_layer = [4.,3,1]

class Node:
    def __init__(self):
        self.children = []
        self.name = ''.join([random.choice(string.ascii_letters) for i in range(3)])

    def make_child(self, current_layer, node_per_layer):
        if current_layer >= len(node_per_layer):
            return
     
        for i in range(node_per_layer[current_layer]):
            self.children.append(Node())
        
        self.children[0].make_child(current_layer + l, node_per_layer)

        for i in range(0, len(self.children) ):
            self.children[i].children = self.children[0].children[:]
new_node = Node()
new_node.make_child(0,node_per_layer)

