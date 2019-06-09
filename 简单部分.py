"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# 时间复杂度o(n**2)
# def two_nums(nums, target):
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if target == nums[i] + nums[j]:
#                 return [i, j]
#
#     return ("没有这个值")
#
#
# nums = [2, 7, 11, 15]
# target = 10
# res = two_nums(nums, target)
# print(res)


# 时间复杂度o(n)
# def two_nums(nums, target):
#     dic = {}
#     for k, v in enumerate(nums):
#         i = target - v
#         if i in dic:
#             return [dic.get(i), k]
#         dic[v] = k
#
#
# nums = [2, 7, 11, 15]
# target = 13
# res = two_nums(nums, target)
# print(res)



























