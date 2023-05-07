def city_country(city, country, population=""):
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted

print(city_country("bratislava", "slovakia"))