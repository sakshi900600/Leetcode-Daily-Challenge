# Total Waviness of Numbers in Range I

# Input: num1 = 4848, num2 = 4848
# Output: 2
# Explanation:
# Number 4848: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.


# Approach:
# Need to count no of peaks (digit strictly greater than both of its immediate neighbors) and valleys(digit strictly less than both of its immediate neighbors) for each no from num1 to num2.

# simply run a loop in that given range
# for each no, convert it to string and check for peaks and valleys by comparing each digit with its neighbors. If it is a peak or valley, increase the count by 1.
# return count



class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """

        cnt = 0
        for digit in range(num1, num2+1):
            cnt += self.cntpeakval(digit)
        
        return cnt
        
    
    def cntpeakval(self, num):
        li = str(num)
        if len(li) <= 2:
            return 0
        
        cnt = 0
        for i in range(1, len(li)-1):
            if (li[i]>li[i-1] and li[i]>li[i+1]) or (li[i]<li[i-1] and li[i]<li[i+1]):
                cnt += 1
        
        return cnt

