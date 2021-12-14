weight_in_kilogram = float(input("Please enter your weight in kilograms: "))
height_in_meters = float(input("Please enter your hight in meters: "))
print(f'Your Body Mass Index is:\
 {round(weight_in_kilogram/(height_in_meters*height_in_meters), 2)}')