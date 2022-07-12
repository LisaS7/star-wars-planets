from app import planets

def list_from_string(string):
    return [item.strip() for item in string.split(',')]

climates = []
for planet in planets:
    climates.extend(list_from_string(planet.climate))

unique_climates = set(climates)

list2 = []
climates2 = [list2.extend(list_from_string(planet.climate)) for planet in planets]
print(list2)