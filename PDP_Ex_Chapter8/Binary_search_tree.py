class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_right(self, valueRight):
        self.right = valueRight

class Tree:
    def __init__(self, node):
        self.node = node

    def __str__(self):
        currNode = self.node
        string = "The Node value is: " + str(self.node.value)
        index = 1
        currNode = self.node.right
        while (currNode is not None):
            string += "\n |" + "-" * index + "The Node value is: " + str(currNode.value)
            index +=1
            currNode = currNode.right
        return string

    def look_up(self, lookValue):
        currNode = self.node
        while(currNode is not None):
            if currNode.value == lookValue:
                return True
            currNode = currNode.right
        return False

    def remove(self, removeNode):
        currNode = self.node
        prevNode = None
        while(currNode is not None):
            if currNode.value == removeNode.value:
                prevNode.insert_right(currNode.right)
                return
            prevNode = currNode
            currNode = currNode.right

class Main:
    if __name__== "__main__":
        base = Node(10)
        node1 = Node(15)
        node2 = Node(20)
        node3 = Node(25)
        t = Tree(base)
        print(t)
        base.insert_right(node1)
        node1.insert_right(node2)
        node2.insert_right(node3)
        print(t)
        print("Look if 20 in the tree: " + str(t.look_up(20)))
        print("Look if 100 in the tree: " + str(t.look_up(100)))
        #t.remove(node1)
        t.remove(node3)
        print(t)
        