###########################################################################
#                               Data Structures                           #
#                                                                         #
#   Programmed by Maxwell Solko (02/26/2018)                              #
#   Class:  CS300                                                         #
#   Instructor:  Nathaniel Miller                                         #
#                                                                         #
#   Description:  This assignment is about data structures.  We are       #
#                 creating a Linked List, doubly Linked List, stack,      #
#                 queue, and deque.                                       #
#                                                                         #
###########################################################################


###########################################################################
#                                Node                                     #
#   This is the 'Node' class which is used as building blocks for the     #
#   Linked List class.  All of it's methods are simple get and set        #
#   methods (with O(1)).                                                  #
###########################################################################

class Node():

    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# The previous node isn't used in the Linked List, but will be
# used for doubly Linked Lists.  
    def get_pre(self):
        return self.previous_node

    def set_pre(self, new_previous):
        self.previous_node = new_previous

###########################################################################
#                            Linked List                                  #
#   This is the 'Linked List' class which is a chain of nodes.  The list  #
#   knows the first node, then each node knows their data and what the    #
#   next node is. There is no 0th index for this linked list.             #
###########################################################################

class LinkedList(object):
    def __init__(self, first_node=None):
        self.first_node = first_node

# Adding is a constant function, setting the first node then the next_node
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.first_node)
        self.first_node = new_node

# Removing is linear, since it needs to go through the list to the index being removed
    def remove(self, item):
        current_node = self.first_node
        previous = None
        found = False
        #same system as search, but remembers the previous node
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        # if the first node is the one you want to remove, this happens.
        if previous is None:
            self.first_node = current_node.get_next()
        # otherwise, it changed the link to skip the "removed" node
        else:
            previous.set_next(current.get_next())

# Search is linear, going through each node and checking for the item
    def search(self, item):
        current_node = self.first_node
        found = False
        # checks each node if it has the item you are looking for
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
        # if you get to the end of the list, this happens
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        return True

# Size is linear for this linked list.  It goes through the list and adds 1 for each node.
    def size(self):
        current_node = self.first_node
        count = 0
        while current_node: #once the current node gets to an empty node it will stop
            count += 1
            current_node = current_node.get_next()
        return count
    
# isEmpty is constant, checking if there is a first node or not.
    def isEmpty(self):
        if self.first_node == None:
            return True
        else:
            return False

# Appending is linear since it needs to get to the end of the list to append.
    def append(self, item):
        current_node = self.first_node
        previous = None
        while current_node:
            previous = current_node
            current_node = current_node.get_next()
        # this only happens if there isn't anything in the list.
        if previous is None:
            new_node = Node(item)
            new_node.set_next(self.first_node)
            self.first_node = new_node
        # if things were in the list, it adds a new node to the end.
        else:
            previous.set_next(Node(item))

# Index is linear for the same reason as all other linear methods so far.
# this is essentially a combination of search and size (both linear)
    def index(self, item):
        current_node = self.first_node
        found = False
        count = 0
        # checks each node if it has the item you are looking for
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
                count += 1
        # if you get to the end of the list, this happens
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        else:
            return count+1

# Insert is linear, needing to go through more nodes the bigger pos is.
    def insert(self, pos, item):
        if self.size() < pos:
            print("List isn't long enough for position given.")
            return
        previous = None
        current_node = self.first_node
        for i in range (0, pos):
            previous = current_node
            current_node = current_node.get_next()
        if previous is None:
            new_node = Node(item)
            new_node.set_next(self.first_node)
            self.first_node = new_node
        else:
            new_node = Node(item)
            new_node.set_next(current_node) # sets the link from the new node
            previous.set_next(new_node) # sets a link to the new node

# Pop is linear, going to the position (or end) through each node.
# if pos is left empty, it removes the last item.
    def pop(self, pos=None):
        if self.isEmpty():
            print("List is empty, cannot pop anything.")
            return
        if pos==None:
            current_node = self.first_node
            previous = None
            previous_2 = None #this is 2 nodes behind the current node
            while current_node: #once the current node gets to an empty node it will stop
                previous_2 = previous 
                previous = current_node
                current_node = current_node.get_next()
            if previous_2 is None: #only occurs if one thing is in the list
                self.remove(previous.get_data())
            else:
                previous_2.set_next(None)
            return previous.get_data()
        else:
            if self.size() < pos:
                print("List isn't long enough for position given.")
                return
            previous = None
            current_node = self.first_node
            for i in range (1, pos):
                previous = current_node
                current_node = current_node.get_next()
            if previous is None: # only happens if the position is 1
                self.remove(self.first_node.get_data())
            else: # makes the list skip the node
                previous.set_next(current_node.get_next())
            return current_node.get_data()


###########################################################################
#                             Doubly Linked List                          #
#   This is the 'doublly-Linked List' class which is a chain of nodes.    #
#   The list is almost equivalent to a regular linked list, there is just #
#   a use of the node's previous_node attribute to go backwords through   #
#   the list.                                                             #
###########################################################################

class DoublyLinkedList(object):
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
        
# add is changed if there isn't anything in the list.
    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.first_node)
        # if empty, it changes the last node as well
        if self.isEmpty():
            self.last_node = new_node
        self.first_node = new_node

# Removing is linear like the linked list remove
    def remove(self, item):
        current_node = self.first_node
        previous = None
        found = False
        #same system as search, but remembers the previous node
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                previous = current_node
                current_node = current_node.get_next()
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        # if the first node is the one you want to remove, this happens.
        if previous is None:
            self.first_node = current_node.get_next()
            return
        temp_node = current_node.get_next()
        # if the item isn't the last node, it does this.
        if temp_node:
            previous.set_next(current_node.get_next())
            current_node = current_node.get_next()
            current_node.set_pre(previous)
        # if it is the last node, this happens
        else:
            previous.set_next(None)
            self.last_node = previous

# Search is equivalent to linked list search.
    def search(self, item):
        current_node = self.first_node
        found = False
        # checks each node if it has the item you are looking for
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
        # if you get to the end of the list, this happens
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        return True

# Size is equivalent to linked list size
    def size(self):
        current_node = self.first_node
        count = 0
        while current_node: #once the current node gets to an empty node it will stop
            count += 1
            current_node = current_node.get_next()
        return count

# isEmpty equivalent to linked list.
    def isEmpty(self):
        if self.first_node == None:
            return True
        else:
            return False

# Appending is constant since it just uses the get previous methods
    def append(self, data):
        new_node = Node(data)
        new_node.set_pre(self.last_node)
        # if empty, it changes the first node as well
        if self.isEmpty() is True:
            self.first_node = new_node
            self.last_node = new_node
        else:
            self.last_node.set_next(new_node)
            self.last_node = new_node

# Index is equivalent to linked list index
    def index(self, item):
        current_node = self.first_node
        found = False
        count = 0
        # checks each node if it has the item you are looking for
        while current_node and found is False:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()
                count += 1
        # if you get to the end of the list, this happens
        if current_node is None:
            print(str(item) + " is not found in the list.")
            return
        else:
            return count+1

# Insert is linear, needing to go through more nodes the bigger pos is.
# insert can't put something at the end; use append for that.
    def insert(self, pos, item):
        if self.size() < pos:
            print("List isn't long enough for position given.")
            return
        previous = None
        current_node = self.first_node
        for i in range (0, pos):
            previous = current_node
            current_node = current_node.get_next()
        # if the first node where you add (and didn't use add), this happens.
        if previous is None:
            new_node = Node(item)
            new_node.set_next(self.first_node)
            self.first_node = new_node
        else:
            new_node = Node(item)
            new_node.set_next(current_node)
            new_node.set_pre(previous)

# Pop without a position is now constant, using the last_node
# Pop with a position is linear, going to the position through each node.
    def pop(self, pos=None):
        if self.isEmpty():
            print("List is empty, cannot pop anything.")
            return
        if pos==None:
            current_node = self.last_node
            #only occurs if one thing is in the list
            if current_node.get_pre():
                temp_node = current_node.get_pre()
                self.last_node = temp_node
                temp_node.set_next(None)
            else:
                self.remove(current_node.get_data())
            return current_node.get_data()
        else:
            if self.size() < pos:
                print("List isn't long enough for position given.")
                return
            previous = None
            current_node = self.first_node
            for i in range (1, pos):
                previous = current_node
                current_node = current_node.get_next()
            if previous is None: # only happens if the position is 1
                self.remove(self.first_node.get_data())
                return current_node.get_data()
            temp_node = current_node.get_next()
            if temp_node: # if the position is in the middle, this happens
                previous.set_next(temp_node)
                temp_node.set_pre(previous)
            else: #if the position is the last position, this happens.
                # occurs if one thing is in the list
                if previous is None: 
                    self.remove(current_node.get_data())
                else:
                    temp_node = current_node.get_pre()
                    self.last_node = temp_node
                    temp_node.set_next(None)
            return current_node.get_data()




###########################################################################
#                                 Question 3                              #
#   Python's list isn't a Linked-List nor a Doubly-Linked-List.  The main #
#   argument would be that indexing, or giving the value at a certain     #
#   point in the list is constant for Pythin's list, and there isn't a    #
#   way to do that with either LL or DLL.                                 #
#                                                                         #
###########################################################################


###########################################################################
#                                   Stack                                 #
#   This is the 'Stack' class which uses Python's list.  Every single     #
#   method has constant running time, since it only ever adds or takes out#
#   from the end, and looks at the length of the list, which is constant. #
###########################################################################

class StackList(object):
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        temp = self.list.pop()
        self.list.append(temp)
        return temp
    
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.list)

###########################################################################
#                                   Queue                                 #
#   This is the 'Queue' class which uses our Doubly-Linked List class.    #
#   The queue only cares about what is at the beginning and end of the    #
#   queue, which makes the DLL very convenient.                           #
###########################################################################

class Queue(object):
    def __init__(self):
        self.queue = DoublyLinkedList()

# Enqueue just uses the append method, so the running time is equal (O(1))
    def enqueue(self, item):
        self.queue.append(item)
        return

# Dequeue just uses the pop method, so the running time is equal (O(n))
# since n is always 1 in this case, it is O(1)
    def dequeue(self):
        return self.queue.pop(1)

# IsEmpty just uses the same method, so the running time is equal (O(1))
    def isEmpty(self):
        return self.queue.isEmpty()

# Size just uses the same method, so the running time is equal (O(n))
    def size(self):
        return self.queue.size()
        
###########################################################################
#                                   Deque                                 #
#   This is the 'Deque' class which uses our Doubly-Linked List class.    #
#   The deque only cares about what is at the beginning and end of the    #
#   deque, which makes the DLL very convenient.                           #
###########################################################################

class Deque(object):
    def __init__(self):
        self.deque = DoublyLinkedList()
        
# addFront is DoublyLinkedList's add, so the running time is O(1)
    def addFront(self, item):
        self.deque.add(item)
        return

# addRear is Queue's enqueue, so the running time is O(1)
    def addRear(self, item):
        self.deque.append(item)
        return

# removeFront is equal to the Queue's dequeue, so it's running time is O(1)
    def removeFront(self):
        return self.deque.pop(1)

# removeRear is pop (no position) so the running time is O(1)
    def removeRear(self):
        return self.deque.pop()

# IsEmpty just uses the same method, so the running time is equal (O(1))
    def isEmpty(self):
        return self.deque.isEmpty()

# Size just uses the same method, so the running time is equal (O(n))
    def size(self):
        return self.deque.size()

###########################################################################
#                           Reverse Polish Notation                       #
#   Reverse Polish Notation is a method of computing arithmetic so that   #
#   parenthesis aren't needed.  Transforming a regular expression into    #
#   RPN is a different question entirely--All I'm doing is using the      #
#   notation to compute the expression.                                   #
###########################################################################

# This will work as long as the function has a correct amount of operators
# and numbers, as well as you using the corrent operator signs
# * not x  for multiplication, and / not ÷ for division.
def RPN(function):
    fstack = StackList()
    split = function.split()
    for i in range(len(split)):
        if split[i] == "+":
            temp1 = fstack.pop()
            temp2 = fstack.pop()
            temp3 = int(temp2) + int(temp1)
            fstack.push(temp3)
##            print("Debug: ", fstack.peek())
        elif split[i] == "-":
            temp1 = fstack.pop()
            temp2 = fstack.pop()
            temp3 = int(temp2) - int(temp1)
            fstack.push(temp3)
##            print("Debug: ", fstack.peek())
        elif split[i] == "*":
            temp1 = fstack.pop()
            temp2 = fstack.pop()
            temp3 = int(temp2) * int(temp1)
            fstack.push(temp3)
##            print("Debug: ", fstack.peek())
        elif split[i] == "/":
            temp1 = fstack.pop()
            temp2 = fstack.pop()
            temp3 = int(temp2) / int(temp1)
            fstack.push(temp3)
##            print("Debug: ", fstack.peek())
        else:
            fstack.push(split[i])
##            print("Debug: ", fstack.peek())
    if fstack.size() != 1:
        return "Something is wrong with the function, more than one thing is in the stack after processing."
    else:
        return fstack.pop()



