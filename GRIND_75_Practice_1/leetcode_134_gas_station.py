class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Checking if there is a solution
        if sum(gas) < sum(cost):
            return -1

        total_cost = 0
        starting_index = 0

        for i in range(len(gas)):
            total_cost += gas[i] - cost[i]

            if total_cost < 0:
                starting_index = i+1
                total_cost = 0
        return starting_index


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
