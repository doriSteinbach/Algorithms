from Heap import Heap
import unittest

class HeapTestCase(unittest.TestCase):
    
    def test_small_heap(self):
        heap = Heap([3,2,1])
        
        self.assertEqual(heap.to_array(), [1,2,3])
        
unittest.main()
