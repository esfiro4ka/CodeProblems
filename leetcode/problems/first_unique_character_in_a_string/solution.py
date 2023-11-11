class Solution:
    def firstUniqChar(self, s: str) -> int:
        # первое решение
        count = defaultdict(int)
        for e in s:
            count[e] += 1
        for key, value in count.items():
            if value == 1:
                return s.find(key)
        return -1
        
#         альтернативное решение
#         count = defaultdict(int)
#         unique_indices = {}

#         for i, e in enumerate(s):
#             count[e] += 1

#             if count[e] == 1:
#                 unique_indices[e] = i
#             elif count[e] > 1 and e in unique_indices:
#                 del unique_indices[e]

#         return next(iter(unique_indices.values()), -1)
            
            