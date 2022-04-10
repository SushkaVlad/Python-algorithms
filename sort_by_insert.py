def find_the_smallest(lst):
    ind = 0
    smallest = lst[0]
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            ind = i
    return ind


def sort(lst):
    sorted_lst = list()
    for i in range(len(lst)):
        smallest_ind = find_the_smallest(lst)
        sorted_lst.append(lst.pop(smallest_ind))
    return sorted_lst


print(sort([5, 7, 3, -56, 0, 8]))
