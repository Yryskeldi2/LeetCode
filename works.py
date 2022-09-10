# task 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap = {}
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]] 


# task 2
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         ans = []
#         def backtrack(S = [], left = 0, right = 0):
#             if len(S) == 2 * n:
#                 ans.append("".join(S))
#                 return
#             if left < n:
#                 S.append("(")
#                 backtrack(S, left+1, right)
#                 S.pop()
#             if right < left:
#                 S.append(")")
#                 backtrack(S, left, right+1)
#                 S.pop()
#         backtrack()
#         return ans

