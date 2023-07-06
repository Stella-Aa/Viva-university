import math


def calculate_distance(coordinate_first, coordinate_second):
    latitude1, longitude1 = coordinate_first
    latitude2, longitude2 = coordinate_second
    radius = 6371  # radius of the Earth in kms

    latitude1 = math.radians(latitude1)
    longitude1 = math.radians(longitude1)
    latitude2 = math.radians(latitude2)
    longitude2 = math.radians(longitude2)

    # Haversine formula to calculate distance between two points
    d_latitude = latitude2 - latitude1
    d_longitude = longitude2 - longitude1
    a = math.sin(d_latitude / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(d_longitude / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance


def find_nearest_location(my_location, other_locations):
    nearest_loc = None
    nearest_distance = float('inf')
    for location in other_locations:
        distance = calculate_distance(my_location, location)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_loc = location
    return nearest_loc


# Example
my_location = (40.7128, -74.0060)  # New York City coordinates
other_locations = [
    (34.0522, -118.2437),  # Los Angeles coordinates
    (51.5074, -0.1278),  # London coordinates
    (35.6895, 139.6917)  # Tokyo coordinates
]

nearest_location = find_nearest_location(my_location, other_locations)
print("Nearest location:", nearest_location)
