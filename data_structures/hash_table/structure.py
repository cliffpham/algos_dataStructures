from dll import DoublyLinkedList

class HashTable():
    def __init__(self):
        # convert self.space into an array
        self.space = [0] * 10
        #self.space = {}

    # based on: https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key
    def generate_hash(self, key):
        if isinstance(key, basestring):
            result = 0
            for i in range(len(key)):
                result += ord(key[i])
            key = result
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key

    def insert_item(self, key, value):
        hash_key = self.generate_hash(key)
    # hash key needs to be converted into a single digit integer to determine array index
        convert_key = hash_key % 7
        table = self.space
        if not convert_key in table:
            linked_list = DoublyLinkedList()
            linked_list.insert_node(key, value)
            self.space[convert_key] = linked_list
        else:
            existing_list = table[convert_key]
            existing_list.insert_node(key, value)

    def find_key(self, key):
        hash_key = self.generate_hash(key)
        convert_key = hash_key % 7
        table = self.space
        if convert_key in table:
            existing_list = table[convert_key]
            if existing_list.find_node(key):
                existing_list.traverse_forward()
                return True
        return False

    def remove_key(self, key):
        hash_key = self.generate_hash(key)
        convert_key = hash_key % 7
        table = self.space
        if not self.find_key(key):
            print("Key was not found")
            return
        else:
            table[covert_key].remove_node(key)
            del table[convert_key]
        
    def print_hash_table(self):
        print(self.space)


hash_table = HashTable()
hash_table.insert_item(317, "first item")
hash_table.insert_item(700, "second_item")
#hash_table.insert_item(21, "third_item")
hash_table.print_hash_table()
print(hash_table.space[2].traverse_forward())
#print(hash_table.find_key(700))
#print(hash_table.space[0].traverse_forward(hash_table.space[0].head))
#hash_table.remove_key(700)
#hash_table.print_hash_table()
#hash_table.remove_key("Bob")
#hash_table.insert_item("Bob", True)
#hash_table.print_hash_table()
#hash_table.find_key("Bob")
#print(hash_table.space[0].traverse_forward(hash_table.space[0].head))
