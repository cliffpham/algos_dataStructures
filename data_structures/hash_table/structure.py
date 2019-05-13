from dll import DoublyLinkedList

class HashTable():
    def __init__(self):
        self.space = {}

    def generate_hash(self, key):
        return key % 7

    def insert_item(self, key, value):
        hash_key = self.generate_hash(key)
        table = self.space
        if not hash_key in table:
            linked_list = DoublyLinkedList()
            linked_list.insert_node(key, value)
            self.space[hash_key] = linked_list
        else:
            existing_list = table[hash_key]
            existing_list.insert_node(key, value)

    def find_key(self, key):
        convert_key = self.generate_hash(key)
        table = self.space
        if convert_key in table:
            existing_list = table[convert_key]
            if existing_list.find_node(key):
                return True
        return False

    def remove_key(self, key):
        convert_key = self.generate_hash(key)
        table = self.space
        if not self.find_key(key):
            print("Key was not found")
            return
        table[convert_key].remove_node(key)
        
    def print_hash_table(self):
        print(self.space)


hash_table = HashTable()
hash_table.insert_item(317, "first item")
hash_table.insert_item(700, "second_item")
hash_table.insert_item(21, "third_item")
hash_table.print_hash_table()
print(hash_table.space[0].traverse_forward(hash_table.space[0].head))
print(hash_table.find_key(700))
print(hash_table.space[0].traverse_forward(hash_table.space[0].head))
hash_table.remove_key(700)
print(hash_table.space[0].traverse_forward(hash_table.space[0].head))
