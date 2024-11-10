class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to print the linked list
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)))

    # Method to insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to delete the first occurrence of a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to be deleted, keeping track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the value is not present in the list
        if current is None:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    # Method to find a node by value
    def find(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        return current is not None  # Returns True if found, False otherwise

# Creating a Linked List and adding elements
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Linked List after appending elements:")
ll.display()

# Inserting at the beginning
ll.insert_at_beginning(5)
print("\nLinked List after inserting 5 at the beginning:")
ll.display()

# Deleting a node
ll.delete_node(20)
print("\nLinked List after deleting node with value 20:")
ll.display()

# Finding a node
print("\nIs 30 in the list?", ll.find(30))
print("Is 100 in the list?", ll.find(100))
