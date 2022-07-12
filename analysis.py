from app import planets

def list_from_string(string):
    return [item.strip() for item in string.split(',')]

climates = []
for planet in planets:
    climates.extend(list_from_string(planet.climate))

unique_climates = set(climates)
print(unique_climates)

populations = [planet.population for planet in planets if planet.population]
print(sorted(populations))