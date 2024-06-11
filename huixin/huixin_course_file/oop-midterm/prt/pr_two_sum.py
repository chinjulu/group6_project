from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers in the given list such that they add up to the target value.

        Parameters:
            nums (List[int]): The list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two numbers that add up to the target.

        Examples:
            >>> solution = Solution()

            # Example 1:
            >>> nums1 = [2, 7, 11, 15]
            >>> target1 = 9
            >>> result1 = solution.twoSum(nums1, target1)
            >>> sorted(result1) == [0, 1]
            True

            # Example 2:
            >>> nums2 = [3, 2, 4]
            >>> target2 = 6
            >>> result2 = solution.twoSum(nums2, target2)
            >>> sorted(result2) == [1, 2]
            True

            # Example 3:
            >>> nums3 = [3, 3]
            >>> target3 = 6
            >>> result3 = solution.twoSum(nums3, target3)
            >>> sorted(result3) == [0, 1]
            True
        """

        for i in range(len(nums)):
            cp_nums = nums[:]
            remain = target - cp_nums[i]
            ans = []
            ans.append(i)
            cp_nums.remove(nums[i])
            if remain in cp_nums:
                ans.append(cp_nums.index(remain) +1)
                return ans
                break
            

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)