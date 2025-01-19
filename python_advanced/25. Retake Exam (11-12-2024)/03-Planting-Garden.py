available_space = 50.0
plant_types = [("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0)]
plant_requests = {"rose": 10, "tulip": 20}

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

if len(planted) == len(plant_requests) and all(planted[plant] == quantity for plant, quantity in sorted_requests if plant in planted):
    print(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    print("Planted plants:")
    print("\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items())))
else:
    print("Not enough space to plant all requested plants!")
    print("Planted plants:")
    print("\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items())))

available_space = 20.0
plant_types = [("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0)]
plant_requests = {"rose": 10, "tulip": 20, "sunflower": 5}

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

if len(planted) == len(plant_requests) and all(planted[plant] == quantity for plant, quantity in sorted_requests if plant in planted):
    print(f"All plants were planted! Available garden space: {available_space:.1f} sq meters.")
    print("Planted plants:")
    print("\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items())))
else:
    print("Not enough space to plant all requested plants!")
    print("Planted plants:")
    print("\n".join(f"{plant}: {pieces}" for plant, pieces in sorted(planted.items())))