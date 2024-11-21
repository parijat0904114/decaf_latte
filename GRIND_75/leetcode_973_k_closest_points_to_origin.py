# MinHeap Solution
import heapq

# Max Heap Solution


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        max_heap_elements = []
        for p in points:
            dist = p[0]*p[0] + p[1]*p[1]
            heapq.heappush(max_heap_elements, [-dist, p])
            # We can safely remove the root element as we set
            # the condition > k.
            if len(max_heap_elements) > k:
                heapq.heappop(max_heap_elements)

        return [p for _, p in max_heap_elements]


# Min Heap Solution


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap_elements = []

        for point in points:
            dist = point[0]**2 + point[1]**2
            heap_elements.append([dist, point])

        heapq.heapify(heap_elements)

        result = []

        while k > 0:
            _, point = heapq.heappop(heap_elements)
            result.append(point)
            k -= 1
        return result

# Optimal Solution
# Lambda Sorting along with Slicing


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Always use .sort() instead of sorted().
        # .sort() does in place sorting.
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # We could return [:k]. However it would cost us
        # some space complexity. To reduce it from O(k) to O(1)
        # the following while loop is used.
        while k != len(points):
            points.pop()
        return points


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
