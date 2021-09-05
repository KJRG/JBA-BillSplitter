# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
number_of_filled_groups = int(input())
filled_groups = dict.fromkeys(groups)
for i in range(0, number_of_filled_groups):
    number_of_children_in_group = int(input())
    group = groups[i]
    filled_groups[group] = number_of_children_in_group
print(filled_groups)
