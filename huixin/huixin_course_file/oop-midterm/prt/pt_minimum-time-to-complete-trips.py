from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        Returns the minimum time required for all buses to complete at least the given number of totalTrips.

        Parameters:
            time (List[int]): An array of integers representing the time taken by each bus to complete one trip.
            totalTrips (int): An integer representing the number of trips all buses should make in total.

        Returns:
            int: The minimum time required for all buses to complete at least totalTrips trips.

        Examples:
            >>> solution = Solution()
            >>> time1 = [1, 2, 3]
            >>> totalTrips1 = 5
            >>> solution.minimumTime(time1, totalTrips1)
            3

            >>> time2 = [2]
            >>> totalTrips2 = 1
            >>> solution.minimumTime(time2, totalTrips2)
            2
        """
        check = lambda t: sum( t // e for e in time) >= totalTrips
        low = 0
        high = time[0] * totalTrips
        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else:
                low = mid + 1
        return low
    
        ''' this code exceeds time limit
        tot_time = 0
        for i in range(10**7):
            tot_trip = 0
            tot_time += 1
            for e in time:
                tot_trip += tot_time // e 
                if tot_trip >= totalTrips:
                    # print (tot_trip)
                    return tot_time'''
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)