def list_roman_emperors(*emperors_info, **emperors_years):
    successful = []
    unsuccessful = []

    for emperor, status in emperors_info:
        if status:
            successful.append(emperor)
        else:
            unsuccessful.append(emperor)


    emperors = {}
    for emperor, years in emperors_years.items():
        emperors[emperor] = years


    sorted_successful = sorted(
        [(emperor, emperors[emperor]) for emperor in successful],
        key=lambda x: (-x[1], x[0])
    )

    sorted_unsuccessful = sorted(
        [(emperor, emperors[emperor]) for emperor in unsuccessful],
        key=lambda x: (x[1], x[0])
    )


    result = []
    total_emperors = len(emperors_info)

    result.append(f"Total number of emperors: {total_emperors}")


    if sorted_successful:
        result.append("Successful emperors:")
        for emperor, years in sorted_successful:
            result.append(f"****{emperor}: {years}")


    if sorted_unsuccessful:
        result.append("Unsuccessful emperors:")
        for emperor, years in sorted_unsuccessful:
            result.append(f"****{emperor}: {years}")

    return "\n".join(result)
