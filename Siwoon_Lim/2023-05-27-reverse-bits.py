# Time Complexity: O(1).
# Space Complexity: O(1).

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Initialize the reversed number to 0
        reversed_num = 0

        # Iterate over all 32 bits of the given number
        for i in range(32):
            # Left shift the reversed number by 1 and add the last bit of the given number to it
            reversed_num = (reversed_num << 1) | (n & 1)
            n >>= 1
        return reversed_num
