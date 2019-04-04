class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # first, append to the storage we have
        self.storage.append(value)
        # then, we need to siftUp, or bubble up the value
        self._bubble_up(len(self.storage) - 1, self.storage)

    def delete(self):
        self.swap(0, len(self.storage) - 1, self.storage)
        valueToDelete = self.storage.pop()
        self._sift_down(0, len(self.storage) - 1, self.storage)

        return valueToDelete

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index, storage):
        parentIdx = (index - 1) // 2
        # while we are not at top ofheap
        while index > 0 and storage[index] > storage[parentIdx]:
            self.swap(index, parentIdx, storage)
            index = parentIdx
            parentIdx = (index - 1) // 2

    def _sift_down(self, index, endIdx, storage):
        # modified sift down to take in a currentIdx and endIdx

        leftChildIdx = index * 2 + 1
        # keep going until we run out of childnodes to swap
        while leftChildIdx <= endIdx:
            rightChildIdx = index * 2 + 2 if index * 2 + 2 <= endIdx else -1
            if rightChildIdx is not -1 and storage[rightChildIdx] > storage[leftChildIdx]:
                # swap those indexes
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if storage[idxToSwap] > storage[index]:
                self.swap(index, idxToSwap, storage)
                index = idxToSwap
                leftChildIdx = index * 2 + 1
            else:
                break

    def swap(self, i, j, storage):
        # added a swap helper func

        storage[i], storage[j] = storage[j], storage[i]
