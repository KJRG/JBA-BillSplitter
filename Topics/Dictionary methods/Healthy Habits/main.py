# the list "walks" is already defined
# your code here
distance_sum = 0
number_of_walks = 0
for walk_data in walks:
    distance_sum += walk_data.get("distance")
    number_of_walks += 1
mean_distance = distance_sum // number_of_walks
print(mean_distance)
