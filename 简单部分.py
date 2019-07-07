import time

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

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？
'''

# 通过转换成字符串的方式
# def isPalindrome(num):
#     reverse_num = str(num)[::-1]
#     if str(num) == reverse_num:
#         return True
#     return False
#
# num = 10
# print(isPalindrome(num))

# 通过数字直接判断
# def isPalindrome(num):
#     # 小于0的肯定不是回文数
#     if num < 0:
#         return False
#     # 计算当前数子有几位
#     count = 0
#     num_ = num
#     while num_ >= 1:
#         num_ = num_ / 10
#         count += 1
#     num_l = num
#     while count >= 1:
#         count -= 1
#         num_left = num_l // 10 ** count
#         num_right = num % 10
#         num = num // 10
#         num_l = num_l - num_left * 10 ** count
#         if num_left != num_right:
#             return False
#     return True
#
# num = 1567651
# print(isPalindrome(num))

'''
罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
示例 1:
输入: "III"
输出: 3
示例 2:
输入: "IV"
输出: 4
示例 3:
输入: "IX"
输出: 9
示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''
# 暴力破解
# def roman_numerals(num):
#     strat_time = time.time()
#     roman_dict = {"IV": 4,"IX": 9,"XL": 40,"XC": 90,"CD": 400,"CM": 900,
#                   "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     l = []
#     while len(num) != 0:
#         for k, v in roman_dict.items():
#             if k in num:
#                 num = num.replace(k, "", 1)
#                 l.append(v)
#     finall_num = sum(l)
#     end_time = (strat_time - time.time())
#     print(end_time)
#     return finall_num
#
#
# res = roman_numerals(num="MCMXCIV")
# print(res)

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
"""
# 暴力解法
# def common_prefix(num):
#     # 先计算最短的字符串长度
#     min_len = min([len(i) for i in num])
#     c_pre = ''
#     for i_index in range(min_len):
#         for j in num:
#             if len(c_pre) != i_index + 1 and c_pre != j[i_index]:
#                 c_pre = c_pre + j[i_index]
#             if c_pre and j[i_index] != c_pre[i_index]:
#                 if i_index == 0:
#                     return "输入不存在公共前缀"
#                 return c_pre.replace(c_pre[i_index], "")
#     return c_pre
#
# res = common_prefix(num = ["flower","flow","flowht"])
# print(res)


# 用切片的方式
# def common_prefix(num):
#     num = sorted(num)
#     lenght = len(num[0])
#     pre = ''
#     for i_index in range(lenght):
#         pre = num[0][:i_index + 1]
#         for j in num:
#             if j[:i_index+1] != pre:
#                 return j[:i_index]
#     return pre
#
# res = common_prefix(num = ["flower","flower","flowht"])
# print(res)

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
"""
























