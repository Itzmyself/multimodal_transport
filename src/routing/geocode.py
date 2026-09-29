from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="multimodal_transport_recommender")


def geocode_place(place_name):
    """
    Convert a place name into latitude and longitude.
    """
    location = geolocator.geocode(place_name)

    if location is None:
        return None

    return {
        "place": place_name,
        "latitude": location.latitude,
        "longitude": location.longitude,
    }


if __name__ == "__main__":
    city = input("Enter city: ")

    result = geocode_place(city)

    if result:
        print(result)
    else:
        print("Location not found.")
