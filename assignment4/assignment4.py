import random
import string
NODE_PER_LAYER = [4,3,2]

class Node:
    def __init__(self):
        self.children = []
        self.weight = []
        self.name = ''.join([random.choice(string.ascii_letters) for i in range(3)])

    def make_child(self, current_layer, node_per_layer):
        if current_layer >= len(node_per_layer):
            return
     
        for i in range(node_per_layer[current_layer]):
            self.children.append(Node())
        
        self.children[0].make_child(current_layer + 1, node_per_layer)

        for i in range(1, len(self.children) ):
            self.children[i].children = self.children[0].children[:]
    
    def set_weights(self, current_layer, node_per_layer):
        if current_layer >= len(node_per_layer):
            return
        self.weight = [0.0] * len(self.children)
        for i in range(len(self.children)):
            self.weight[i] = random.uniform(0,1)
            self.children[i].set_weights(current_layer+1,node_per_layer)
        return

    def output_children(self, layer, node_per_layer):
        indent = '    '*layer
        if layer >= len(node_per_layer):
            print(f"{indent} {self.name}")
            return
        print(f"{indent} {self.name} is connected to:")
        for i in range(len(self.children)):
            try:
                print(f"{indent} Weight of {self.weight[i]}")
            except:
                pass
            self.children[i].output_children(layer+1,node_per_layer)
            
        return


master = Node()
master.make_child(0, NODE_PER_LAYER)
master.output_children(0,NODE_PER_LAYER)
master.set_weights(0,NODE_PER_LAYER)
master.output_children(0,NODE_PER_LAYER)

