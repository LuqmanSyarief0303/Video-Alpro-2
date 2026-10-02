# Ask the user for sleeping hours, working, relaxing hours
sleeping_hours = float(input("How many hours do you sleep every day?: "))
working_hours = float(input("How many hours do you work every day?: "))
weekday_relaxing_hours = float(input("How many hours do you spend relaxing per weekday?: "))
weekend_relaxing_hours = float(input("How many hours do you spend relaxing per weekend day?: "))
#Compute available hours
weekday_available_hours = 24 - sleeping_hours - working_hours - weekday_relaxing_hours - 3
weekend_available_hours = 24 - sleeping_hours - weekend_relaxing_hours - 3
total_available_hours = weekday_available_hours * 5 + weekend_available_hours * 2
# Print available hours
print("you have " + str(weekday_available_hours) + " hours to study every working day")
print("you have " + str(weekend_available_hours) + " hours to study every weekend day")
print("Is total, you have " + str(total_available_hours) + " hours to study each week")