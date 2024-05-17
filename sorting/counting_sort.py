def counting_sort(arr):
    counter = [0] * (max(arr) + 1)
    for num in arr:
        counter[num] += 1
    out = []
    for index, number in enumerate(counter):
        if number > 0:
            for _ in range(number):
                out.append(index)
    return out


# print(counting_sort([2, 1, 3, 4, 4, 2, 6, 5]))
"""
Counting Sort is best when we deal with small numbers named as k.
Then the size of the counter would be maximum k.
So we can put the condition k<=n.
Time Complexity: O(n + k)
Space Complexity: O(k)
"""
