def ft_water_reminder():
    water_time = int(input("Days since last watering: "))
    if water_time > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
