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

"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


# 不能提前预测移除情况，只有溢出才会判断溢出了，返回0
# class Solution:
#     def reverse(self, num):
#         a_num = abs(num)
#         a_num = str(a_num)[::-1]
#         if "-" in str(num):
#             num = "-" + a_num
#         else:
#             num = a_num
#
#         if int(num) > 2**31-1 or int(num) < -2**31:
#             num = 0
#
#         return num
#
#
# solution = Solution()
# res = solution.reverse(num=2**29)
# print(res)


# 提前预测将要溢出，可以把所有的数除以10
# class Solution:
#     def reverse(self, num):
#         a_num = abs(num) // 10
#         remainder = abs(num) % 10
#         a_num = str(remainder) + str(int(str(a_num)[::-1])/10)
#         if "-" in str(num):
#             a_num = "-" + str(a_num)
#         if float(a_num) > (2**31-1)/10 or float(a_num) < (-2**31)/10:
#             num = 0
#         else:
#             num = int(str(a_num).replace(".", ""))
#         return num
#
#
# solution = Solution()
# res = solution.reverse(num=2**29)
# print(res)
























