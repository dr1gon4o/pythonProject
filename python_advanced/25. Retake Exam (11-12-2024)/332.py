def plant_garden(garden_space, *allowed_plants, **requested_plants):
    plant_spaces = {plant: space for plant, space in allowed_plants}

    remaining_space = garden_space
    planted = {}

    for plant in sorted(requested_plants.keys()):
        if plant not in plant_spaces:
            continue

        pieces = requested_plants[plant]
        space_needed = plant_spaces[plant] * pieces

        if space_needed <= remaining_space:
            planted[plant] = pieces
            remaining_space -= space_needed
        else:
            possible_pieces = remaining_space // plant_spaces[plant]
            if possible_pieces > 0:
                planted[plant] = int(possible_pieces)
                remaining_space -= possible_pieces * plant_spaces[plant]

    result = []

    all_planted = all(requested_plants[plant] == planted.get(plant, 0)
                      for plant in requested_plants if plant in plant_spaces)

    if all_planted:
        result.append(f"All plants were planted! Available garden space: {remaining_space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    result.append("Planted plants:")
    for plant, count in planted.items():
        result.append(f"{plant}: {count}")

    return "\
".join(result)


# Test the function with the example prints
print("\
Test 1:")
print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))

print("\
Test 2:")
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))

print("\
Test 3:")
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))

print("\
Test 4:")
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
