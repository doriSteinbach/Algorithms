import math

class Heap(): 
    def __init__(self, array):
        self.heap = array
    
    def parent(self, index):
        return math.floor(index / 2)
    
    def left(self, index):
        return 2 * index
    
    def right(self, index):
        return (2 * index) + 1
    
    def max_heapify(self, index, heap_size):
        l = left(index)
        r = right(index)
        if l <= heap_size and self.heap[l] > self.heap[index]:
            largest = l
        else:
            largest = index
        if r <= heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            max_heapify(largest)
            
    def build_max_heap(self):
        mid = math.floor(len(self.heap) / 2)
        for i in range(mid, 0, -1):
            max_heapify(i, len(self.heap))
            
    def heapsort(self):
        build_max_heap()
        for i in range(len(self.heap), 1, -1):
            temp = self.heap[i]
            self.heap[i] = self.heap[0]
            self.heap[0] = temp
            max_heapify(0, i)
            
    def insert(self, value):
        self.heap.append(value)
        max_heapify(len(self.heap) - 1)
        
    def print_heap(self):
        print self.heap
        
    def to_array(self):
        return self.heap