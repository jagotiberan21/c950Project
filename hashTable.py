
# a chaining hash table created using Webinar 1 from c950 course tips
class hashTable:
    # constructor with an initial capacity parameter
    # assigns each element within the array with an empty list which can be filled later
    # space-time complexity is O(1)
    def __init__(self, initial_capacity=10):
        # initializes the hash table with the empty list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # this can both insert a new item into the hash table and update the value if key is already present
    # space-time complexity is O(N)
    def insert(self, key, item):
        # get the linked list where the item will go in the table
        element = hash(key) % len(self.table)
        element_list = self.table[element]

        # updates the corresponding value for the key if key is already in the list
        for kv in element_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if the key is not found in the element's list, the item is inserted to the end of the list
        key_value = [key, item]
        element_list.append(key_value)
        return True

    # searches for an item with matching key in the hash table
    # returns the item if found, or returns None if not found
    # space-time complexity is O(N)
    def search(self, key):
        # get the linked list where the key would be
        element = hash(key) % len(self.table)
        element_list = self.table[element]

        # search for the key in the linked list
        for key_value in element_list:
            # find the item's index and return the item that is in the linked list
            if key_value[0] == key:
                return key_value[1]
            # returns None if the key is not found
            return None

    # removes an item from the hash table if there is a matching key
    # space-time complexity is O(N)
    def delete(self, key):
        # get the linked list where this item will be removed from
        element = hash(key) % len(self.table)
        element_list = self.table[element]

        # removes the item from the linked list if it is present
        for kv in element_list:
            if kv[0] == key:
                element_list.remove([kv[0], kv[1]])
