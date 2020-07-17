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

    def divide(self, dividend, divisor):
        a, b, p, t = abs(dividend), abs(divisor), 0, 1
        sign = (a == dividend) == (b == divisor)
        if a == 0:
            return 0
        if a == b:
            return 1 if sign else -1
        if b == 1:
            res = a if sign else -a
            return min(res, (1 << 31) - 1)
        if a < b:
            return 0
        while a >= b or t > 1:
            if a >= b:
                p += t
                a -= b
                t <<= 1
                b <<= 1
            else:
                t >>= 1
                b >>= 1
        res = p if sign else -p
        return min(res, (1 << 31) - 1)
    
    def match_s(self, s, words):
        if not s or not words:
            return []
        if len(words) > 0:
            if not words[0]:
                return []
        from collections import Counter
        word_map = dict(Counter(words))
        sz = len(words[0])
        cnt = len(words)
        s_sz = len(s)
        res = []
        for i in range(0, s_sz - sz * cnt+1):
            sub_s = s[i:i+sz*cnt]
            tmp_map = {}
            for j in range(0, sz*cnt, sz):
                tmp = sub_s[j:j+sz]
                if tmp not in words:
                    continue
                tmp_map[tmp] = tmp_map.get(tmp, 0) + 1
                if word_map[tmp] < tmp_map[tmp]:
                    continue
            if word_map == tmp_map:
                res.append(i)
        return res
    
    def longestValidParentheses(self, s):
        l1, l2, r1, r2, res = 0, 0, 0, 0, 0
        for idx in range(len(s)):
            c1, c2 = s[idx], s[-idx-1]
            if c1 == '(':
                l1 += 1
            else:
                r1 += 1
            if c2 == '(':
                l2 += 1
            else:
                r2 += 1
            
            if l1 == r1:
                res = max(res, 2 * l1)
            elif l1 < r1:
                l1, r1 = 0, 0
            
            if l2 == r2:
                res = max(res, 2 * l2)
            if l2 > r2:
                l2, r2 = 0, 0
        return res

def binary_search(nums, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if nums[mid] > target:
        return binary_search(nums, target, start, mid-1)
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, end)
    else:
        return mid

def search(nums, target):
    if not nums:
        return - 1
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[-1]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def n_backwards(n):
    if n == 1:
        return '1'
    
    def process(s):
        res = ''
        cur = s[0]
        cnt = 1
        if len(s) == 1:
            return '11'
        for i in range(1, len(s)):
            if s[i] == cur:
                cnt += 1
            else:
                res += '{}{}'.format(cnt, cur)
                cur = s[i]
                cnt = 1
        res += '{}{}'.format(cnt, cur)
        return res
    
    rd = 1
    pre, cur = '', '1'
    while rd < n:
        pre, cur = cur, process(cur)
        rd += 1
    return cur



if __name__ == "__main__":
    for i in range(1, 5):
        print(n_backwards(i))