def plant_garden(garden_space, *allowed_plants, **requested_plants):
    total_space_needed = 0
    plant_spaces = {}

    for plant_type, space in allowed_plants:
        plant_spaces[plant_type] = space

    for plant_type, pieces in requested_plants.items():
        if plant_type not in plant_spaces:
            return f"Unrecognized plant {plant_type} provided! Unable to plant it!"
        total_space_needed += plant_spaces[plant_type] * pieces

    if total_space_needed > garden_space:
        return "Insufficient space!"

    planted_types = []
    for plant_type, pieces in sorted(requested_plants.items()):
        planted_types.append(f"{plant_type}: {pieces}")

    result = "Successfully planted " + " and ".join(planted_types) + "."
    return result

# # Example usage:
# print(plant_garden(5.0, ("tomato", 0.5), ("cucumber", 1.0), tomato=10))
# print(plant_garden(1.0, ("tomato", 0.5), ("cucumber", 1.0), tomato=1, cucumber=1))
# print(plant_garden(0.5, ("tomato", 0.5), ("cucumber", 1.0), tomato=1, cucumber=1))
# print(plant_garden(1.0, ("tomato", 0.5), ("cucumber", 1.0), tomato=1, banana=1))