class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print("Added data as the head node. ",data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print("Added data to the end of the list.", data)

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index should be 1 or greater.")

            if n == 1:
                deleted_value = self.head.data
                self.head = self.head.next
                print(f"Deleted node {n} with value {deleted_value}.")
                return

            current = self.head
            count = 1

            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError(f"Index {n} is out of range.")

            deleted_value = current.next.data
            current.next = current.next.next
            print(f"Deleted node {n} with value {deleted_value}.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    ll = LinkedList()

    # Add nodes
    ll.add_to_end(10)
    ll.add_to_end(20)
    ll.add_to_end(30)
    ll.add_to_end(40)

    # Print list
    ll.print_list()

    # Delete the 3rd node
    ll.delete_nth_node(3)
    ll.print_list()

    # Delete head
    ll.delete_nth_node(1)
    ll.print_list()

    # Try deleting out of range
    ll.delete_nth_node(10)

    # Try deleting from empty list
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
