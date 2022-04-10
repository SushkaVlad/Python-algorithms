def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        el = lst[0]
        less = [i for i in lst if i < el]
        more = [i for i in lst if i > el]
        return quicksort(less) + [el] + quicksort(more)


print(quicksort([5, 7, 3, -56, 0, 8]))
