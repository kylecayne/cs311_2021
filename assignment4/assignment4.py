import random
import string
NODE_PER_LAYER = [4.,3,1]

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
  
    def adjust_weights(self):
        if len(self.children >= 0):
                return
        selfchildren_weights = []
        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0,1))

            self.children[i].adjust_weights()
    
    def output_children(self, layer):
        indent = ''*layer
        if len(self.children) == 0:
            print(f"{indent}{self.node.name}")
            return
        for i in range(len(self.children)):
            self.children[i].output_children(layer+1)

        if i < len(self.children_connection_weights):
            print(f"{indent}with weight {self.children_connection_weights[i]} ")

master = Node()
first_node = Node()
first_node.make_child(0, NODE_PER_LAYER)

master.children.append(first_node)

for i in range(0,len(NODE_PER_LAYER)):
    new_node = Node()
    new_node.children = first_node.children[:]
    master.children.append(new_node)
master.node.output_children(0)
master_node.adjust_weights()
master_node.output_children(0)
