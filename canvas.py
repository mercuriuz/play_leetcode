class Solution:
    def fourSum(self, nums, target):
        n, res = len(nums), []
        if n < 4:
            return res
        nums.sort()
        for idx in range(n-3):
            if nums[idx] + nums[idx+1] + nums[idx+2] + nums[idx+3] > target:
                return res
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            for idxx in range(idx+1, n-2):
                if nums[idx] + nums[idxx] + nums[idxx+1] + nums[idxx+2] > target:
                    break
                if idxx > idx+1 and nums[idxx] == nums[idxx-1]:
                    continue 
                head, tail = idxx+1, n-1
                while head < tail:
                    print(idx, idxx, head, tail)
                    total = nums[idx] + nums[idxx] + nums[head] + nums[tail]
                    if total == target:
                        res.append([nums[idx], nums[idxx], nums[head], nums[tail]])  
                        while head < tail and nums[head] == nums[head+1]:
                            head += 1
                        while head < tail and nums[tail] == nums[tail-1]:
                            tail -= 1
                        head += 1
                        tail -= 1 
                    elif total < target:
                        head += 1
                    else:
                        tail -= 1
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2, -1]
    nums = [-2, -2, 0, 0, 0, 2, 2]
    target = 0
    res = solution.fourSum(nums, target)
    print(res)
