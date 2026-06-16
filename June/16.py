# 3612. Process String with Special Operations I


# Approach:
# Here we have to perform some operations and then return the final string.
# So, I have taken a list and perform all the operations
# At the end join this list and return the ans string


# T.C = O(n)
# S.C = O(n)



class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        li = []
        for ch in s:
            if ch == '#':
                li.extend(li)
            elif ch == '%':
                li.reverse()
            elif ch == '*':
                if len(li) > 0:
                    li.pop()
            else:
                li.append(ch)
        
        return "".join(li)
