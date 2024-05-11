class MinHeap:
    def __init__(self, capacity):
        # defines the maximum number of elements that can be stored in the heap
        self.capacity = capacity
        # defines the current number of elements in the heap
        self.size = 0
        # defines the array to store the elements
        self.arr = []

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def get_min(self):
        if(self.arr):
            return self.arr[0]
        print("heap is empty")

    # removes and returns root of heap arr[0]
    def extract_min(self):
        if(self.size == 0):
            print("heap is empty")
            return
        minimum = self.arr[0]
        if(self.size == 1):
            self.size -= 1
            return self.arr.pop()
        if(self.size > 1):
            self.size -= 1
            self.swap(0, self.size)
            self.min_heapify(0)
        return minimum


    # converts the binary tree to min heap
    # input is a heap and index i at which heapfiy has to be checked
    def min_heapify(self, i:int):
        root = i
        smallest = i
        right = self.right(i)
        left = self.left(i)
        if(left < self.size and self.arr[left] < self.arr[smallest]):
           smallest = left
        if(right < self.size and self.arr[right] < self.arr[smallest]):
           smallest = right
        if(smallest != i):
            self.swap(smallest, i)
            self.min_heapify(smallest)

    # time complexity log(n) or height of tree
    def insert(self, val):
        if(self.size >= self.capacity):
            print("heap is full")
            return
        self.size += 1
        self.arr.append(val)
        if(self.size > 1):
            i = self.size - 1
            p = self.parent(i)
            node = self.arr[i]
            while(i !=0 and self.arr[p] > node):
                self.swap(p, i)
                i = p
                p = self.parent(i)
                node = self.arr[i]
        print(val, "inserted in heap")

    def swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j]= temp

if __name__ == '__main__':
    minHeap = MinHeap(20)
    minHeap.insert(40)
    minHeap.insert(20)
    minHeap.insert(30)
    minHeap.insert(35)
    minHeap.insert(25)
    minHeap.insert(80)
    minHeap.insert(32)
    minHeap.insert(100)
    minHeap.insert(70)
    minHeap.insert(60)
    print("min heap:", minHeap.arr)
    print("minimum:", minHeap.get_min())
    print("extract:", minHeap.extract_min())
    # for i in range(20, 0, -1):
    #     minHeap.insert(i)
    print(minHeap.arr, minHeap.size, minHeap.capacity)