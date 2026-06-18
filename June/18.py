# 1344. Angle Between Hands of a Clock


# Approach:
# This is completely based on math. We have to find out the smaller angle between minute and hour hand in watch.

# angle in 1 min = 360/60 = 6 deg
# angle in 1 hour = 360/12 = 30 deg

# Coz when minute passes hour hand also move due to it. Like when its 3:30 then the hour hand comes in between 3 & 4. So we also need to add that change in hour angle.

# movement due to min: 
# 1 hour = 360/12
# 1 min = 360/12*60 = 0.5 deg
# here doing hour % 12 so that hour come in between 1 to 12

# final hour angle = 30*(hour % 12) + 0.5*min

# at the end take diff
# return the min diff: either the calculated diff or the reverse 360-diff



class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        
        min_angle = 6 * minutes
        hour_angle = 30 * (hour % 12) + 0.5 * minutes

        diff = abs(hour_angle - min_angle)

        return min(diff, 360 - diff)
        
