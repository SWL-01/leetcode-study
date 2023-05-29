# Time complexity: O(n + m) where 'n' is the length of the input list 'digits' and 'm' is the number of digits in the
# resulting number after adding one Space complexity: O(n)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        return [int(i) for i in str(num + 1)]
