class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index],
                    self.data[index]
                )
                index = parent_index
            else:
                break
    
    def heapify_down(self, index):
        size = len(self.data)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and self.data[left].urgency
                < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency
                < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest],
                self.data[index]
            )

            index = smallest
    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Expected a Patient object")

        if not isinstance(patient.urgency, int) or not 1 <= patient.urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[0]
    def remove_min(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        minimum = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return minimum
    def print_heap(self):
        print("Current Queue:")

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")



# Test your MinHeap class here including edge cases

# Test the MinHeap class
heap = MinHeap()

heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

heap.print_heap()

print("\nNext patient:")
next_up = heap.peek()
print(next_up.name, next_up.urgency)

print("\nServing patient:")
served = heap.remove_min()
print(served.name, served.urgency)

heap.print_heap()

# Test edge cases
print("\nTesting empty queue:")
empty_heap = MinHeap()
print(empty_heap.peek())
print(empty_heap.remove_min())

print("\nTesting one patient:")
single_heap = MinHeap()
single_heap.insert(Patient("Riley", 2))
print(single_heap.remove_min().name)
print(single_heap.peek())
