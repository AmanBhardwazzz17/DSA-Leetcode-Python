class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        result = []
        for cx, cy, radius in queries:
            count = 0
            radius_squared = radius * radius
            for px, py in points:
                dx = px - cx
                dy = py - cy
                if dx * dx + dy * dy <= radius_squared:
                    count += 1
            result.append(count)
        return result