from typing import List
from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        frequencies = counts.values()
        return len(set(frequencies)) == 1

sol = Solution()
s = 'abcabc'
print(f'answer: {sol.areOccurrencesEqual(s)}')
