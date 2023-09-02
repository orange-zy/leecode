class Solution:
  # 合并两个有序数组[simple]
  # https://leetcode.cn/problems/merge-sorted-array/
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()
        
        # return nums1
    
        # 指针法
        p1, p2, p = m-1, n-1, m+n-1
        # 将nums2合并至p1
        while p2>=0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        return nums1

    # 返回多数 数量大于 n//2
    def majorityElement(self, nums: List[int]) -> int:
        num = len(nums)//2
        
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            
            if dic[nums[i]] > num:
                return nums[i]
        return -1

    # 三数之和等于0，不重复组合
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left = i+1
            right = len(nums) - 1

            # 着重去重
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
    
                elif curSum > 0:
                    right -= 1
                else:
                    left += 1
    
            
        return result

  # 最接近的三数之和
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nearSum = float("inf")
        nums.sort()
        
        if len(nums) < 3:
            return nearSum
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1

            # 不断更新 左右指针的位置
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if abs(curSum-target) < abs(nearSum-target):
                    nearSum = curSum
                if curSum == target:
                    return curSum

                elif curSum > target:
                    r -= 1
                else:
                    l += 1
                    
        return nearSum

  # 存在重复元素
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        # 利用字典
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                dic[nums[i]] += 1
                if dic[nums[i]] > 1:
                    return True
            else:
                dic[nums[i]] = 1
        
        return False


  # 有效的字母异位词，将同样字母组成的字符进行分组
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str in dic.keys():
                dic[sort_str].append(str)
            else:
                dic[sort_str] = [str]
        return list(dic.values())
