# Time  Complexity: O(N*logN)
# Space Complexity: O(N)
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]


def main():
    run = KthLargest(3, [4, 5, 8, 2])
    print(KthLargest.add(run, 3))
    print(KthLargest.add(run, 5))
    print(KthLargest.add(run, 10))
    print(KthLargest.add(run, 9))
    print(KthLargest.add(run, 4))


if __name__ == '__main__':
    main()
