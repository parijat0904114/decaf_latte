def change_var(num):
    if num == 0:
        return 0
    return num + change_var(num-1)


print(change_var(5))
