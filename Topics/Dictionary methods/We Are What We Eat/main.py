# the list "meals" is already defined
# your code here
total_kcal = sum(meal.get("kcal") for meal in meals)
print(total_kcal)
