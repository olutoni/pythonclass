alien_0 = {
    "color": "green",
    "points": 5
}

print(alien_0["color"])
print(alien_0["points"])

alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

alien_0["color"] = "yellow"

print(alien_0)
print(
    f'The alien color is now {alien_0["color"]} and position is {alien_0["y_position"]}')

alien_0["speed"] = "medium"
print(alien_0)

if alien_0["speed"] == "slow":
    counter = 1
elif alien_0["speed"] == "medium":
    counter = 2
else:
    counter = 3

alien_0["x_position"] = alien_0["x_position"] + counter
print(alien_0)

print(alien_0.get("point"))
