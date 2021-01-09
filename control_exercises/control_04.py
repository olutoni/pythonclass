# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')


play_again = True
while play_again:
    alien_color = input("Enter alien color: ")
    if alien_color.lower() == "green":
        print("you just earned 5 point")
    elif alien_color.lower() == "yellow":
        print("You just earned 10 points")
    elif alien_color.lower() == "red":
        print("You just earned 15 points")
    play_continue = input("Do you want to play again (yes/no): ")
    if play_continue.lower() == "no":
        play_again = False
