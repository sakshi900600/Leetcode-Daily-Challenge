# 



class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """

        if n == 1:
            return r - l + 1

        MOD = 10**9 + 7

        inc = [0] * (r + 2)
        dec = [0] * (r + 2)

        for x in range(l, r + 1):
            inc[x] = 1
            dec[x] = 1

        for _ in range(2, n + 1):
            newInc = [0] * (r + 2)
            newDec = [0] * (r + 2)

            # Prefix sum for increasing transitions
            prefix = 0
            for x in range(l, r + 1):
                newInc[x] = prefix
                prefix = (prefix + dec[x]) % MOD

            # Suffix sum for decreasing transitions
            suffix = 0
            for x in range(r, l - 1, -1):
                newDec[x] = suffix
                suffix = (suffix + inc[x]) % MOD

            inc = newInc
            dec = newDec

        ans = 0
        for x in range(l, r + 1):
            ans = (ans + inc[x] + dec[x]) % MOD

        return ans

        
        