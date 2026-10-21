print("Welcome to the Treasure Hunt!")
print("You must pass through 4 rooms to find the treasure. Each room has a challenge that you must complete to move on to the next room.")
print("Choose 'left' or 'right' for each door.\n")

# Room 1 - Left
door1 = input("Room 1: The secret passage is ahead. Which way does the secret passage go? (left/right): ").lower()

if door1 == "left":
    print("✓ YOu entered correctly! The path behind the door opens up.\n")

    # Room 2 - Extension logic
    # Correct path to continue is 'right', but 'left' gives a bonus message and continues the game.
    door2 = input("Room 2: A strange light appears! Go left or right? (left/right): ").lower()

    if door2 == "left":
        print("BONUS! - ✓ You found an ancient map hinting that 'right' is the way forward.\n")
        print("The bonus clue was noted. The path continues.")
        bonus = True

        # proceed to room 3 if we reached here, both choices allow progression past the 2nd room.
    elif door2 == "right":
        print("✓ You entered correctly! You continue on the path.\n")
    else:
        print("× Invalid choice. You must choose 'left' or 'right'. Game over.")
        exit()

    # Room 3 - Correct path is 'right'
    door3 = input("Room 3: The path splits. Which way do you go? (left/right): ").lower()

    if door3 == "right":
        print("✓ You entered correctly! The path continues.\n")
        
        # Room 4 - Correct path is 'left'
        door4 = input("Room 4: The final challenge! Which way do you go? (left/right): ").lower()

        if door4 == "left":
            print("✓ You entered correctly! You have found the treasure! 🎉 Congratulations!\n")
            if bonus:
                print("BONUS! - You found the ancient map in Room 2, which helped you find the treasure faster!")
        elif door4 == "right":
            print("× You chose the wrong path. The treasure is lost. Game over.")
            exit()
        else:
            print("× Invalid choice. You must choose 'left' or 'right'. Game over.")
            exit()
    elif door3 == "left":
        print("× You chose the wrong path. Game over!")
        exit()
elif door1 == "right":
    print("× You chose the wrong path. Game over!")
    exit()
else:
    print("× Invalid choice. You must choose 'left' or 'right'. Game over.")
    exit()
