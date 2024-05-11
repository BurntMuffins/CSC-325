import sys

DEBUG = False

class Heap:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = [None]
        
    def getData(self):
        return self.data[:self.size]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0

    def __siftUp(self, child):
        parent = (child - 1) // 2
        while (child > 0) and (self.data[child] > self.data[parent]):
            temp = self.data[child]
            self.data[child] = self.data[parent]
            self.data[parent] = temp
            if DEBUG:
                print(f"{self.data[parent]} swapped with {self.data[child]}")
            child = parent
            parent = (child - 1) // 2

    def buildFrom(self, seq):
        self.data = [None]*len(seq)
        self.size = self.capacity = len(seq)

        for x in range(self.size):
            self.data[x] = seq[x]
            
        index = (2 * self.data.index(seq[0])) + 1

        while (index < len(seq)):
            self.__siftUp(index)
            index += 1

    def addToHeap(self, newVal):
        if (self.size == self.capacity):
            self.capacity *= 2
            temp = [None] * self.capacity
            
            for i in range(self.size):
                temp[i] = self.data[i]
                
            self.data = temp

        self.data[self.size] = newVal
        self.__siftUp(self.size)
        self.size += 1
        
        return newVal

    def __largestChild(self, index, lastIndex):
        ''' Inputs:
            - index -> index of the current node
            - lastIndex -> index of the last node in the heap
            Output:
            - index of the largest child if it exists, None otherwise
        '''

        ### WRITE YOUR CODE HERE###
        # Find the indexes of the right and left children
        leftChildIndex = 2 * index + 1
        rightChildIndex = 2 * index + 2

        # If there is no children then return None
        if leftChildIndex >= lastIndex:
            return None
        
        # Compare the values of the children and return in the larger child's index
        if self.data[leftChildIndex] > self.data[rightChildIndex]:
            return leftChildIndex
        else:
            return rightChildIndex
        
    def __siftDownFromTo(self, fromIndex, last):
        ''' Inputs:
            - fromIndex -> index of the node where to start sifting from
            - last -> index of the last node in the heap
            Output:
            - the node sifted down as far as necessary to maintain heap conditions
        '''    
        ### WRITE YOUR CODE HERE###
        currIndex = fromIndex
        while currIndex < last:
            # Finding the index of the largest child
            largestChild = self.__largestChild(currIndex, last)
            # If there is no larger child then return the current value
            if largestChild == None:
                return self.data[currIndex]
            
            # If ther largest child is larger than the parent then swap the values
            if self.data[largestChild] > self.data[currIndex]:
                self.data[largestChild], self.data[currIndex] = self.data[currIndex], self.data[largestChild]
                currIndex = largestChild
            # Else return the current value
            else:
                return self.data[currIndex]
            
    def sort(seq):
        
        h = Heap()
        h.buildFrom(seq)
        
        for i in range(len(seq)):
            h.data[0], h.data[h.size - 1] = h.data[h.size - 1], h.data[0]
            h.size -= 1
            h.__siftDownFromTo(0, h.size - 1)
        return h.data
        
    def __str__(self):
        st = f"\tHeap size: {(self.size)}.\n"
        st += f"\tHeap capacity: {(self.capacity)}.\n"
        st += f"\tElements of heap: \n"
        for x in range(self.size):
            st += f"\t\tValue: {(self.data[x])} at index: {x}\n"
        return st 
    def __repr__(self):
        return self.__str__()

def main():

    file = open(sys.argv[1], "r")
    for line in file:
        values = [int(x) for x in line.split()]
        
    print(f"Original list: {values}\n")

    ### WRITE YOUR CODE HERE###
    h = Heap()
    h.buildFrom(values)
    print(f"Heapified list:\n{h}")
    
    sorted_list = Heap.sort(values)
    print(f"Sorted list: {sorted_list}")

main()
