class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.size += 1

    def findMedian(self) -> float:
        if self.size == 0:
            return self.arr[0]

        if self.size % 2 != 0:
            return self.arr[self.size // 2]
        ind = self.size // 2
        return (self.arr[ind] + self.arr[ind - 1]) / 2