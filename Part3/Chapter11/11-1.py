#hash table can find or delete in O(1)
class HashTable:
    potential_length = [11, 41, 71, 131, 251, 541, 761, 1091, 1181]

    def __init__(self):
        self._length = 0
        self._rate = 0
        self._count = 0
        self._list = [(None, None)
                      for i in range(self.potential_length[self._length])]

    def add(self, key, value, list=None):
        if list == None:
            list = self._list
        index = key % self.potential_length[self._length]
        while index < len(list):
            if list[index][0] == None:
                list[index] = (key, value)
                if list == self._list:
                    self._count += 1
                    self.extend()
                return True
            else:
                index += 1
        return False

    def extend(self):
        if self._count / len(self._list) > 0.6:
            self.rehase()
        else:
            return

    def rehase(self):
        self._length += 1
        new_list = [(None, None)
                    for i in range(self.potential_length[self._length])]
        for i in self._list:
            if i[0] != None:
                self.add(i[0], i[1], list=new_list)
        self._list = new_list

a = HashTable()
