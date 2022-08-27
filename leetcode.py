# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 sum=nums[i]+nums[j]
#                 if sum==target:
#                     return [i,j]
                


# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#     for i in range(len(nums1)):
#         for j in range(i+1,len(nums1)):
#             print(i,j)
# findMedianSortedArrays(self, nums1: List[int], nums2: List[int])

a=[1,3]
b=[2,4]
i=0
while i<len(a):
    # print(a+b)
    i=i+1
print(sorted(a+b))

