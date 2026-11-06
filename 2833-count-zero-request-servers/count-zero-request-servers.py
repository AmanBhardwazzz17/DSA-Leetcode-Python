from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ans = [0] * len(queries)
        freq = [0] * (n + 1)
        left = right = active = 0

        for q, i in sorted((q, i) for i, q in enumerate(queries)):
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if freq[server] == 0:
                    active += 1
                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                freq[server] -= 1
                if freq[server] == 0:
                    active -= 1
                left += 1

            ans[i] = n - active

        return ans