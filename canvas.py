from functools import lru_cache
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

    def mergeTwoLists(self, l1, l2):
        dummy0, dummy1 = ListNode(0), ListNode(0)
        dummy0.next = dummy1

        while l1.next is not None and l2.next is not None:
            val1, val2 = l1.val, l2.val
            if val1 < val2:
                dummy1.next = l1
                l1 = l1.next
            else:
                dummy1.next = l2
                l2 = l2.next
            dummy1 = dummy1.next
        
        if l1:
            dummy1.next = l1
        if l2:
            dummy1.next = l2
            
        return dummy0.next.next

    def generateParenthesis(self, n):
        results = []
        def back(combination, left, right):
            if len(combination) == 2 * n:
                results.append(''.join(combination))
                return
            if left < n:
                combination.append('(')
                back(combination, left+1, right)
                combination.pop()
            if right < left:
                combination.append(')')
                back(combination, left, right+1)
                combination.pop()
        back([], 0, 0)
        return results

    @lru_cache(None)
    def generateParenthesis1(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis1(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
if __name__ == "__main__":
    solution = Solution()
    n = 3
    res = solution.generateParenthesis1(n)
    print(res)
