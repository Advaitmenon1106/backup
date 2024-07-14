class Node():
    def __init__(self, name, parent=None):
        from pandas import DataFrame
        self.name = name
        self.rvs = {}
        self.parent = parent
        self.probs = DataFrame(self.rvs)

    def __repr__(self) -> str:
        return self.name


class Network():
    def __init__(self) -> None:
        self.nodelist = []

    def add_node(self, node_obj, parent=None):
        if parent != None and parent not in [node.name for node in self.nodelist]:
            raise Exception('Parent not in nodelist. Try again.')
        elif len([node for node in self.nodelist if node.parent == None])>0:
            raise Exception('Every bayesian network has to be a DCG (Directed Cyclic Graph); i.e., network cannot have >1 root node.')
        else:
            self.nodelist.append(node_obj)

b = Network()
rain = Node('rain', None)
b.add_node(rain, None)
# b.add_node(rain, None) # -> testing the exception
print(b.nodelist)
