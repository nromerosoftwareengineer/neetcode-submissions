class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Early exit: smallest possible sum already > 0
            if nums[i] > 0:
                break

            j, k = i + 1, n - 1
            target = -nums[i]

            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # Skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1

        return ans