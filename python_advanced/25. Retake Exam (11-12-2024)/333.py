def plant_garden(available_space, *plant_types, **plant_requests):
    planted = {}

    sorted_requests = sorted(plant_requests.items())

    for plant, quantity in sorted_requests:
        space_per_plant = next((space for p_type, space in plant_types if p_type == plant), None)

        if space_per_plant is None:
            continue

        max_plants = int(available_space // space_per_plant)
        plants_to_plant = min(quantity, max_plants)

        if plants_to_plant > 0:
            planted[plant] = plants_to_plant
            available_space -= plants_to_plant * space_per_plant

        if available_space < 0.01:
            break

    all_planted = all(planted.get(plant, 0) == plant_requests[plant] for plant in plant_requests)

    if all_planted:
        return f"All plants were planted! Available garden space: {available_space:.1f} sq meters.\n" + \
               "Planted plants:\n" + \
               "\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items()))
    else:
        return "Not enough space to plant all requested plants!\n" + \
               "Planted plants:\n" + \
               "\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items()))

# # Examples
# print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
# print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
# print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
# print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), tulip=20, daisy=1))