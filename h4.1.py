list1 = list(range(0, int(input())))
list2 = list(range(0, int(input())))

list1 = [int(input()) for i in list1]
list2 = [int(input()) for j in list2]

print(list1)
print(list2)

list_merge = list1 + list2
list3 = set(list_merge)
list_merge = list(list3)


def sort_list(array):
    if len(array) < 2:
        return array
    else:
        n = array[0]
        less = [i for i in array[1:] if i <= n]
        greater = [i for i in array[:] if i > n]
        return sort_list(less) + [n] + sort_list(greater)


print(sort_list(list_merge))
