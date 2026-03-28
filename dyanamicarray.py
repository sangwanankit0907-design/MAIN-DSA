class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [0] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Empty"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self, new_cap):
        new_arr = [0] * new_cap
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_cap