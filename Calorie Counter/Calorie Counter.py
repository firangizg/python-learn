# get the date of today in any format
date = input("What is today's date?: ")

# ask for the calories eaten for every meal during the day and convert them to integer
breakfast = int(input("Breakfast calories eaten: "))
lunch = int(input("Lunch calories eaten: "))
dinner = int(input("Dinner calories eaten: "))
snack = int(input("Snack calories eaten: "))

# add all the calories in a new variable 
total = breakfast + lunch + dinner + snack

# print out the total, but first convert it to string
print("Calorie content for " + date + ": " + str(total))
