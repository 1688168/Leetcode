class MedianFinder:

    def __init__(self):
        """
        : keep mnq size 1 > or equal do mxq .size
        : start from push to mnq.
        : anything greater than mnq[0], push to mnq and rebalance

        """
        self.mnq=[]
        self.mxq=[]


    def addNum(self, num: int) -> None:
        def rebalance():
            if len(self.mnq) > len(self.mxq)+1:
                heappush(self.mxq, heappop(self.mnq)*-1)
            elif len(self.mxq) > len(self.mnq):
                heappush(self.mnq, heappop(self.mxq)*-1)

        if not self.mnq or num > self.mnq[0]:
            heappush(self.mnq, num)
        else:
            heappush(self.mxq, -num)

        rebalance()

    def findMedian(self) -> float:
        if len(self.mnq) > len(self.mxq):
            return self.mnq[0]
        else:
            return (self.mnq[0]+(-self.mxq[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
