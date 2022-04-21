from hashTable import *

# create a hash table that we will populate with the package data for fast 
package_hash = hashTable(40)

class Package:

    def __init__(self, id, address, city, state, zip_code, deadline, weight, special_notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
