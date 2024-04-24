# list

list_numbers: list = [i for i in range(10)]

# main methods

list_numbers.append(12)  # to add 12 on the end of list

list_numbers.pop(0)  # to remove the first item of list

list_numbers.remove(4)  # to remove 4 of list

list_numbers.sort()  # to order the list items

del list_numbers[2]  # to delete the second element on the list

print(list_numbers.clear())  # to delete all elements

print(list_numbers)


# =============================================================

# tuple: tuples are like lists, but immutable

tuple_numbers = tuple(i for i in range(10))

tuple_numbers.index(3)  # return the index of 3

tuple_numbers.count(4)  # shows the number of times 4 appears in the list

print(tuple_numbers)
