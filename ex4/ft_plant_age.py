def ft_plant_age():
    harvest_time = int(input("Enter plant age in days: "))
    if harvest_time > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
