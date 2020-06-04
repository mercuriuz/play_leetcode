class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        curr = nums[0] + nums[1] + nums[2]
        nums.sort()
        for idx in range(len(nums)-2):
            head, tail = idx+1, len(nums)-1

            if nums[idx] + nums[idx+1] + nums[idx+2] > target:
                if abs(nums[idx] + nums[idx+1] + nums[idx+2] - target) < abs(curr - target):
                    curr = nums[idx] + nums[idx+1] + nums[idx+2]
                break
            if nums[-1] + nums[-2] + nums[-3] < target:
                if abs(nums[-1] + nums[-2] + nums[-3] - target) < abs(curr - target):
                    curr = nums[-1] + nums[-2] + nums[-3]
                continue

            while head < tail:
                tmp = nums[idx] + nums[head] + nums[tail]
                if abs(tmp-target) < abs(curr-target):
                    curr = tmp
                if tmp > target:
                    tail -= 1
                elif tmp < target:
                    head += 1
                else:
                    return target
        return curr