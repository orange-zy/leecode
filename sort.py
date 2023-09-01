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
