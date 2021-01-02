distance_km = input("Enter distance in kilometers: ")

if distance_km.isnumeric():
    distance_km = int(distance_km)

    if distance_km < 1:
        print("enter a positive distance")
    else:
        distance_miles = distance_km/0.6214
        print(f"{distance_km}km is {distance_miles} miles")
else:
    print("You have not entered an integer")
