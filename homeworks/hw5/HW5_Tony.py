#Create a class for Nodes
class Node:
    def __init__(self, value):
        # Prevent for bad input
        if type(value) != int:
            print("# WARNING: Please enter an integer!")
        else:
            # Store the value and set the default link to None
            self.value = value
            self.after = None

    # returns the value of the Node
    def __str__(self):
        return str(self.value)

# Create a class for LinkedList
class LinkedList:
    def __init__(self, value):
        # Prevent for bad input
        if type(value) != int:
            print("# WARNING: Please enter an integer!")
        else:
            # create a head node that has the assigned value
            self.head = Node(value)

    # define a function measuring the length of the linkedlist
    def length(self):
        count = 0
        node = self.head
        # Counting the nodes one by one
        while node != None:
            count += 1
            node = node.after
        return count

    # define a function for adding a node at the end
    def addNode(self, new_value):
        # prevent bad input
        if type(new_value) != int:
            print("# WARNING: Please enter an integer!")
        else:
            # create a new node
            new_node = Node(new_value)
            node = self.head
            # pass down from the head node to the end of the list
            while node.after != None:
                node = node.after
            # when it reaches the end node, link the new node to the list
            node.after = new_node

    # define a function for adding node after a given node position
    def addNodeAfter(self, new_value, after_node):
        # prevent bad input
        if type(new_value) != int or type(after_node) != int:
            print("# WARNING: Please enter two integers!")
        elif after_node <= 0:
            print("# WARNING: Please enter a positive integer for the second input!")
        elif after_node > self.length():
            print("# WARNING: The second input exceeds the length of the LinkedList!")
        else:
            # create a new node to be added in
            new_node = Node(new_value)
            node = self.head
            count = 1
            # find the correct position to add the node
            while count < after_node:
                count += 1
                node = node.after
            # add the node to the list
            new_node.after = node.after
            node.after = new_node

    # define a function for adding a new node before a given position
    def addNodeBefore(self, new_value, before_node):
        # prevent bad input
        if type(new_value) != int or type(before_node) != int:
            print("# WARNING: Please enter two integers!")
        elif before_node <= 0:
            print("# WARNING: Please enter a positive integer for the second input!")
        elif before_node > self.length():
            print("# WARNING: The second input exceeds the length of the LinkedList!")
        else:
            # create a new node
            new_node = Node(new_value)
            # If the given position is 1, then we need to switch the head node to the new node
            # and then link the new node to the original linkedlist
            if before_node == 1:
                new_node.after = self.head
                self.head = new_node
            else:
                # if the given position is not 1, then just find the correct position to add the node
                node = self.head
                count = 2
                while count < before_node:
                    count += 1
                    node = node.after
                # adding the new node
                new_node.after = node.after
                node.after = new_node

    # define a function to remove a node from a given position
    def removeNode(self, node_to_remove):
        # prevent bad input
        if type(node_to_remove) != int:
            print("# WARNING: Please enter an integer!")
        elif node_to_remove <= 0:
            print("# WARNING: Please enter a positive integer!")
        elif node_to_remove > self.length():
            print("# WARNING: The input exceeds the length of the LinkedList!")
        else:
            # if the node to be removed is the head node
            # then set the second node to be the head node
            node = self.head
            if node_to_remove == 1:
                self.head = self.head.after
            else:
                # otherwise find the correct position of the node
                # and link the node before to the node after, so that the node is removed
                count = 2
                while count < node_to_remove:
                    count += 1
                    node = node.after
                node.after = node.after.after

    # define a function to remove all the nodes with a given value
    def removeNodesByValue(self, value):
        # prevent bad input
        if type(value) != int:
            print("# WARNING: Please enter an integer!")
        else:
            # first, check if the head node need to be removed
            # because if so, then the head note need to be reset
            node = self.head
            while node is self.head:
                # if there is nothing after the head node and the head node need to be removed
                # then the list becomes "Null"
                if node.after == None:
                    if node.value == value:
                        self.head = None
                    else:
                        # If the head node doesn't need to be removed and there is nothing behind it
                        # then break the loop
                        break
                else:
                    # else check the head node first and then check the second node
                    if node.value == value:
                        # if the head node need to be removed
                        # set the second node to be the new head node
                        self.head = self.head.after
                        node = self.head
                    else:
                        if node.after == None:
                            break
                        else:
                            # if the second node need to be removed
                            # link the head node to the third node
                            if node.after.value == value:
                                node.after = node.after.after
                            else:
                                node = node.after
            # once we done with the head node and the second node
            # we could use a while loop to find out all others
            while node.after != None:
                # find the node that is right before the node to be removed
                if node.after.value == value:
                    # link that node to the node right after the node to be removed
                    node.after = node.after.after
                else:
                    node = node.after

    # define a function for reversing the linkedlist
    def reverse(self):
        # create a new reversed linkedlist with the same head node
        reverselist = LinkedList(self.head.value)
        # starting the second node in the old linkedlist, create a new node with the same value
        node = self.head.after
        while node != None:
            new_head = Node(node.value)
            # link the new node to the head of the reversed list
            new_head.after = reverselist.head
            # set the new node to be the new head node of the reversed list
            # this process adds each node in the old list to the front of the new list one by one
            # so that at the end of the day the old list will be reversed
            reverselist.head = new_head
            node = node.after
        return reverselist

    # define a function to print out the linkedlist
    def __str__(self):
        printstr = ""
        node = self.head
        while node != None:
            printstr = printstr + str(node.value) + " -> "
            node = node.after
        printstr = printstr + "Null"
        return printstr

# some testing code
linkedlist1 = LinkedList(0.5)
linkedlist1 = LinkedList(0)
print(linkedlist1)
linkedlist1.addNode(1.5)
linkedlist1.addNode(15)
print(linkedlist1)
linkedlist1.addNode(12)
print(linkedlist1)
linkedlist1.addNode(37)
print(linkedlist1)
linkedlist1.addNodeAfter(35, 2)
linkedlist1.addNodeAfter(3.5, 2)
print(linkedlist1)
linkedlist1.addNodeBefore(23, 1)
linkedlist1.addNodeBefore(23, 189)
print(linkedlist1)
linkedlist1.addNodeBefore(9, 5)
print(linkedlist1)
print(linkedlist1.length())
linkedlist1.removeNode(30)
linkedlist1.removeNode(3)
print(linkedlist1)
linkedlist1.removeNodesByValue("hahah")
linkedlist1.removeNodesByValue(23)
print(linkedlist1)
print(linkedlist1.reverse())
print(linkedlist1.length())

# more testing code
linkedlist1 = LinkedList(10)
linkedlist1.addNode(15)
linkedlist1.addNode(15)
linkedlist1.addNode(15)
linkedlist1.addNode(15)
linkedlist1.addNode(10)
linkedlist1.addNode(10)
linkedlist1.addNode(15)
linkedlist1.addNode(15)
linkedlist1.addNode(10)
linkedlist1.addNode(15)
print(linkedlist1)
print(linkedlist1.length())
linkedlist1.removeNodesByValue(10)
print(linkedlist1)
linkedlist1.addNodeAfter(3, 4)
linkedlist1.addNodeAfter(3, 4)
linkedlist1.addNodeAfter(5, 2)
linkedlist1.addNodeAfter(3, 4)
linkedlist1.addNodeAfter(7, 1)
linkedlist1.addNodeAfter(7, 8)
print(linkedlist1)
linkedlist1 = linkedlist1.reverse()
print(linkedlist1)
linkedlist1.removeNodesByValue(15)
print(linkedlist1)

# even more testing code
linkedlist1 = LinkedList(10)
print(linkedlist1)
linkedlist1.removeNode(1)
print(linkedlist1)
print(linkedlist1.length())
