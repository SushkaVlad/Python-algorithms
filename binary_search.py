def binary_search(lst, elm):
    left, right = 0, len(lst) - 1
    while left <= right:
        cur = (right + left)//2
        guess = lst[cur]
        if guess == elm:
            return cur
        if guess > elm:
            right = cur - 1
        else:
            left = cur + 1
    return None

print(binary_search([1, 6, 7, 9, 15], 7))

