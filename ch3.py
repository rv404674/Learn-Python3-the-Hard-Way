cars = 100
space_in_cars = 100
passengers = 90
drivers = 20
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")

