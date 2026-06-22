# 1189. Maximum Number of Balloons


# Approach:
# Count freq of all char in balloon and get the minimum freq and that much balloon is present in given text.


# T.C = O(n)
# S.C = O(5)


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        freq = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for ch in text:
            if ch in freq:
                freq[ch] += 1
        
        b = freq.get('b')
        a = freq.get('a')
        l = freq.get('l')
        o = freq.get('o')
        n = freq.get('n')

        return min(b,a,l//2,o//2,n)

