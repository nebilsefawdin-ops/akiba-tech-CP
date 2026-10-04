Destination=input("Enter your travel destination: ")
Distance=float(input("Enter the distance to your destination in kilometers: "))
Average_speed=float(input("Enter your average speed in kilometers per hour: "))
Travel_time=Distance/Average_speed

print(f"destination: {Destination}")
print(f"distance: {Distance} km")
print(f"average speed: {Average_speed} km/h")
print(f"travel time: {Travel_time} hours")