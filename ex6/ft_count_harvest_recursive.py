def ft_count_harvest_recursive(harvest_days=None, current_day=1):
    if harvest_days is None:
        harvest_days = int(input("Days until harvest: "))

    if harvest_days <= 0:
        print("Harvest time!")
        return

    if current_day > harvest_days:
        print("Harvest time!")
        return

    print(f"Day {current_day}")
    ft_count_harvest_recursive(harvest_days, current_day + 1)
