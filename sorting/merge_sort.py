def divide(list):
    list_len = len(list)
    if list_len == 1:
        return list

    mid = list_len // 2
    left_list = divide(list[:mid])
    right_list = divide(list[mid:])
    merged = conquer(left_list, right_list)
    return merged


def conquer(l, r):
    output = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            output.append(l[i])
            i += 1
        else:
            output.append(r[j])
            j += 1

    output.extend(l[i:])
    output.extend(r[j:])
    return output


# Test the function with the array [3, 1, 5, 4]
print("Starting Merge Sort")
sorted_list = divide([5, 4, 3, 2, 1])
print("Final Sorted List:", sorted_list)
