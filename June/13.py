# 3838. Weighted Word Mapping


# Approach:
# I first created a dct with reverse mapping of char.
# Traversed the words list and for each word first got the idx by doing  ord(ch)-ord('a') then got value of it from weights list.
# added into a var and take mod with 26
# added the char into an ans string
# return ans


# T.C = O(n*10)
# S.C = O(26)


class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        
        dct = {
            0: 'z', 1: 'y', 2: 'x', 3: 'w', 4: 'v', 
            5: 'u', 6: 't', 7: 's', 8: 'r', 9: 'q', 
            10: 'p', 11: 'o', 12: 'n', 13: 'm', 14: 'l', 
            15: 'k', 16: 'j', 17: 'i', 18: 'h', 19: 'g', 
            20: 'f', 21: 'e', 22: 'd', 23: 'c', 24: 'b', 
            25: 'a'
        }

        ans = ""

        # print(ord('a'))
        # print(ord('b'))

        # print(ord('b') - ord('a'))
        # print(ord('d') - ord('a'))

        for word in words:
            wt = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                wt += weights[idx]
            
            wt = wt % 26
            ans += dct.get(wt)
        
        return ans
