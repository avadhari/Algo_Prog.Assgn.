from sys import stdin

class minHeap:
    # Initializing the heap list with all values default as -1 as Input values would be either 0 or positive
    # cur-size is the pointer to no. of elements in the heap at a time
    def __init__(self, max_size):
        self.heap = [-1]*(max_size+1)
        self.cur_size = 0

    # Returns Index of Parent Node Element
    def parent_index(self,idx):
        return idx//2

    # Returns Index of Left Child Node Element
    def left_child_index(self,idx):
        return 2*idx

    # Returns Index of Right Child Node Element
    def right_child_index(self,idx):
        return (2*idx)+1

    # Checks whether the accessed node element is leaf
    def isleaf(self, idx):
        return (idx > self.cur_size//2)

    # Min Heapify Method to rearrange the List elements as per Heap Order after Element Extraction
    def minHeapify(self,idx):

        if not self.isleaf(idx):

            if self.heap[idx] > self.heap[self.left_child_index(idx)] or self.heap[idx] > self.heap[self.right_child_index(idx)]:
                # Checks if Right Child is Present
                if self.heap[self.right_child_index(idx)] != -1:
                    # Index of Child Element with Minimum Value of both the childs
                    minOfChildIdx = self.left_child_index(idx) if self.heap[self.left_child_index(idx)] < self.heap[self.right_child_index(idx)] else self.right_child_index(idx)
                else:
                    # Just one Child then by default it would be Left Child
                    minOfChildIdx = self.left_child_index(idx)

                # Swapping the Values appropriately to follow the Heap Order
                self.heap[idx], self.heap[minOfChildIdx] = self.heap[minOfChildIdx],self.heap[idx]
                # Again Checking for the Tree starting from the Chils's Node
                self.minHeapify(minOfChildIdx)

    # Inserting the Element to the heap appropriately Set as position which follows Heap Order
    def A_insert_heap(self,input_num):

        self.cur_size += 1
        cur_index = self.cur_size
        self.heap[cur_index] = input_num

        # Iteratively Checking for the Parent Node's Value and Compare, so as to Inserted Element Reaches appropriate position
        while(self.heap[cur_index] < self.heap[self.parent_index(cur_index)]):
            parent_idx = self.parent_index(cur_index)
            self.heap[cur_index],self.heap[parent_idx] = self.heap[parent_idx],self.heap[cur_index]
            cur_index= parent_idx

    # Extracting Minimum which in Min Heap would be Root Element that is Heap[1] and Rearranging with Heapify
    def E_extract_min(self):

        min = self.heap[1]
        self.heap[1] = self.heap[self.cur_size]
        self.cur_size -= 1
        self.minHeapify(1)
        # Changing last element again to -1 as it's deafult value
        self.heap[self.cur_size+1]=-1

        return min

# List to take lines of Input Text one by one
lines = []
for line in stdin:
    lines.append(line.rstrip())

MinHeap = minHeap(len(lines))

# Result List for storing the Final Output
result = []

for line in lines:
    if line:
        if line[0] == 'A':
            # As the first element is A, second is blank space, 3rd onwards we take and convert to Integer
            insert_input = int(line[2:])
            # As A command stands for Inserting to the Heap we pass the Number to be Inserted
            MinHeap.A_insert_heap(insert_input)
        elif line[0] == 'E':
            # As E command stands for Extracting hence we just Append the Minimum to Final Result List
            result.append(MinHeap.E_extract_min())

# Printing the Final Output to the Standar Output
for r in result:
    print(r)







