from data import plants


def search_plants(keyword: str):
    results = []
    for index, plant in enumerate(plants.plants):
        if (
            keyword.lower() in plant.science_name.lower()
            or keyword.lower() in plant.en_name.lower()
            or keyword.lower() in plant.id_name.lower()
        ):
            results.append(index)

    return results
