class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job, priority):
        self.heap.append((priority, job))
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index][0] > self.heap[parent][0]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def extract_max(self):
        if not self.heap:
            return None

        max_job = self.heap[0]

        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._heapify_down(0)

        return max_job

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = \
                    self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def display(self):
        if not self.heap:
            print("Heap is empty")
        else:
            print("Jobs in Heap Order:")
            for priority, job in self.heap:
                print("Job:", job, "Priority:", priority)
h = MaxHeap()
h.insert("Job A", 20)
h.insert("Job B", 35)
h.insert("Job C", 25)
h.insert("Job D", 40)
h.insert("Job E", 30)
print("#MAX HEAP JOB SCHEDULER#")
print("**********************")
h.display()
print("\nJob with Highest Priority:")
print(h.peek())
print("\nDeleting Highest Priority Job:")
print(h.extract_max())
print("\nHeap after deletion:")
h.display()
print("\nJob with Highest Priority:")
print(h.peek())
