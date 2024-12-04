# Problem :- Choose a mode of transportation based on the distance (e.g., < 3km : walk, 3 - 15km : Bike, > 15km : Car).

distance = int(input("Enter how much distance you want to travel KM: "))

if distance > 0 and distance < 3:
    print("i suggest perfer walk!")
elif distance > 3 and distance < 15:
    print("i suggest perfer bike!")
elif distance > 15:
    print("i suggest perfer car!")
else:
    exit()