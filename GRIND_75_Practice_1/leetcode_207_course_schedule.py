# Topological Sort & BFS

from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        in_degree = [0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        course_queue = deque(course for course in range(numCourses) if in_degree[course] == 0)
        print(course_queue)

        courses_taken = 0

        while(course_queue):
            current_course = course_queue.popleft()
            courses_taken += 1

            for neighbour in graph[current_course]:
                in_degree[neighbour] -=1
                if in_degree[neighbour] == 0:
                    course_queue.append(neighbour)


        return courses_taken == numCourses
            

s = Solution()
print(s.canFinish(2, [[1,0]]))