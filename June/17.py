# 3614. Process String with Special Operations II

# Same as yesterdays problem. Here we have to return kth char instead of whole string

# Brute force is same but gives TLE

class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        li = []

        for ch in s:
            if ch == '*':
                if len(li) > 0:
                    li.pop()
            elif ch == '#':
                li.extend(li)
            elif ch == '%':
                li.reverse()
            else:
                li.append(ch)

        if len(li) <= k:
            return '.'
        
        return li[k]
                


# In this approach: 
# 1. reverse is taking n time
# 2. extend li doubles the size of list and when list size is doubled than cost of operations on string increases significantly . So we need to find a way to optimize it.

# We need to return kth char at the end so instead of creating & maintaining whole list if we only track kth char somehow then that should work.

# Now observe:

# Operation: '*' (pop last character)
# Forward: length n → n-1, removes char at position n-1
# Backward: 
#   - if k == clen (position of removed char): return '.'
#   - else: k stays same, clen += 1 (going back to before pop)

# Operation: '#' (duplicate)
# Forward: length n → 2n, [original] + [original]
# Backward:
#   - k = k % (clen // 2)  # map to position in original
#   - clen //= 2           # length before duplication

# Operation: '%' (reverse)
# Forward: length n → n, reverses entire string
# Backward:
#   - k = clen - 1 - k    # mirror position
#   - clen stays same



# Algo:
# Step 1: Compute final length by going forward (track only length, not string) and through this length we will trace from back.
# Step 2: If k >= final_length → return '.'
# Step 3: Trace k backward through operations
# Step 4: Return the character found

# Time: O(n) where n = len(s)
# Space: O(1)



class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)

        length = 0
        for ch in s:
            if ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1
        
        clen = length
        if k >= clen:
            return '.'
        
        for i in range(n-1,-1,-1):
            ch = s[i]

            if ch == '*':
                if k == clen:
                    return '.'
                clen += 1 # doing + coz from back it is str before removal
            
            elif ch == '#':
                half = clen // 2
                k = k % half
                clen = half
            elif ch == '%':
                k = clen - k - 1
            else:
                if k == clen - 1:
                    return ch
                clen -= 1
        

        return '.'

        