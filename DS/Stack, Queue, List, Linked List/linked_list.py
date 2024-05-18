class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to the next node

class SimpleLinkedList:
    def __init__(self):
        self.head = None  # Head node of the list (initially None)

    # Adds a new node with the given data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return # Nothing to return
        current_node = self.head
        while current_node.next:  # Find the last node
            current_node = current_node.next
        current_node.next = new_node  # Link the last node to the new node

    # Removes the first node from the list
    def remove_first(self):
        if self.head is None:
            return  # Nothing to remove
        removed_data = self.head.data
        self.head = self.head.next  # Update head to point to the second node
        return removed_data

# Example usage
my_list = SimpleLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

removed_data = my_list.remove_first()  # removed_data will be 10

print(f"Removed: {removed_data}")

my_list.append(40)

print("List contents:")
current_node = my_list.head
while current_node:
    print(current_node.data)
    current_node = current_node.next