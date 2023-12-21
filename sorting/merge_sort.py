def divide(list, depth=0):
    indent = "  " * depth  # indentation for better visualization
    print(f"{indent}Dividing: {list}")

    list_len = len(list)
    if list_len == 1:
        return list

    mid = list_len // 2
    left_list = divide(list[:mid], depth + 1)
    right_list = divide(list[mid:], depth + 1)

    merged = conquer(left_list, right_list, depth)
    print(f"{indent}Merged: {merged}")
    return merged


def conquer(l, r, depth):
    indent = "  " * depth  # indentation for better visualization
    print(f"{indent}Conquering: Left {l}, Right {r}")

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

    print(f"{indent}Conquered: {output}")
    return output


# Test the function with the array [3, 1, 5, 4]
print("Starting Merge Sort")
sorted_list = divide([5, 4, 3, 2, 1])
print("Final Sorted List:", sorted_list)
