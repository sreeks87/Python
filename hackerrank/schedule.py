# #
# # Complete the 'maxPresentations' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY scheduleStart
# #  2. INTEGER_ARRAY scheduleEnd
# #



# import heapq,sys

# class Solution(object):
#     def maxEvents(self, a,b):
#         """
#         :type events: List[List[int]]
#         :rtype: int
#         """
#         a.sort(reverse=True)
#         b.sort(reverse=True)
#         min_heap = []
#         result = 0
#         # print(max(events, key=lambda x:x[1])[1])
#         for d in range(min(a), max(b)):
#             # print(d)
#             while a and a[-1] == d:
#                 heapq.heappush(min_heap, a.pop())
#             while min_heap and min_heap[0] == d-1:
#                 heapq.heappop(min_heap)
#             if not min_heap:
#                 continue
            
#             print(min_heap)
#             heapq.heappop(min_heap)
#             result += 1       
#         return result

#     # def maxEvents(self, events) -> int:
#     #     events.sort(key=lambda x: x[0])
#     #     attended = 0
#     #     attending = []
#     #     day = 1
#     #     for start, end in events + [[sys.maxsize, 0]]:
#     #         print(day,start)
#     #         while day < start and attending:
#     #             finish = heapq.heappop(attending)
#     #             if day < finish:
#     #                 attended += 1
#     #                 day += 1
                
#     #         day = max(day, start)
#     #         heapq.heappush(attending, end)
#     #     return attended

# # from functools import lru_cache
# # class Solution:
# #   def maxValue(self, events):
# #     e = sorted(events)

# #     @lru_cache(None)
# #     def dp(i, k):
# #       if k == 0 or i == len(e):
# #         return 0

# #       # binary search events to find the first index j s.t. e[j][0] > e[i][1]
# #       j = bisect.bisect(e, [e[i][1], inf, inf], i + 1)
# #       return max(dp(i + 1, k), e[i][2] + dp(j, k - 1))

# #     return dp(0, k)

# # a=[6,1,2,4]
# # b=[8,7,4,9]

# a=[1,1,2,3]
# b=[4,2,3,3]

# l=[[a[i],b[i]] for i in range(len(a))]

# l=[[6, 8], [1, 9], [2, 4], [4, 7]]

# print(l)
# s=Solution()
# print(s.maxEvents(a,b))


# # print(maxEvents(l))


a=[1,1,2,3]
b=[4,2,3,3]

for i in range(min(a),max(b)+1):
    print(i)