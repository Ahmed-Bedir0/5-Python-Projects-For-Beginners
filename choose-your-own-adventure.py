name = input("What is your name? ")

print("Welcome", name, "to the Lost Kingdom!")
print("You wake up in a dark forest with no idea how you got there.")
print("In front of you is a path that splits in two.")

answer = input(
    "Do you want to go left toward the mountains or right toward the village? "
).lower()

if answer == "left":
    print("You follow the path toward the mountains.")
    print("After an hour, you find an old cave with a torch outside.")

    answer = input(
        "Do you enter the cave or continue up the mountain? "
    ).lower()

    if answer == "cave":
        print("You enter the cave and find a treasure chest.")
        print("Next to it is a rusty sword.")

        answer = input(
            "Do you take the sword or open the chest? "
        ).lower()

        if answer == "sword":
            print("You pick up the sword.")
            print("Suddenly, a giant spider drops from the ceiling!")

            answer = input(
                "Do you fight the spider or run? "
            ).lower()

            if answer == "fight":
                print("You defeat the spider with the sword!")
                print("Behind the spider, you discover a secret passage.")
                print("You follow it and find a room filled with gold.")
                print("You escaped the forest with a legendary sword and a fortune.")
                print("YOU WIN!")

            elif answer == "run":
                print("You run as fast as you can.")
                print("Unfortunately, the spider catches you.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        elif answer == "chest":
            print("You open the chest.")
            print("Inside is a mysterious glowing crystal.")

            answer = input(
                "Do you take the crystal or leave it alone? "
            ).lower()

            if answer == "take":
                print("The crystal suddenly starts glowing brighter.")
                print("A portal opens in front of you!")
                print("You step through it and escape the forest.")
                print("You have discovered the Lost Kingdom.")
                print("YOU WIN!")

            elif answer == "leave":
                print("You decide the crystal is too dangerous.")
                print("You leave the cave and continue your journey.")
                print("Unfortunately, you become lost in the mountains.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        else:
            print("Not a valid option. You lose.")

    elif answer == "mountain":
        print("You continue climbing the mountain.")
        print("You reach the top and see a huge castle in the distance.")

        answer = input(
            "Do you head toward the castle or return to the forest? "
        ).lower()

        if answer == "castle":
            print("You travel toward the castle.")
            print("At the gate, a guard stops you.")

            answer = input(
                "Do you tell the guard the truth or lie about who you are? "
            ).lower()

            if answer == "truth":
                print("You tell the guard everything.")
                print("The guard looks surprised.")
                print("You are the traveler we have been waiting for!")
                print("The gates open and the king welcomes you.")
                print("You have saved the Lost Kingdom!")
                print("YOU WIN!")

            elif answer == "lie":
                print("The guard realizes you are lying.")
                print("You are thrown into the castle dungeon.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        elif answer == "forest":
            print("You return to the forest.")
            print("Night falls, and you become completely lost.")
            print("You lose!")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    print("You follow the path toward the village.")
    print("The village appears completely abandoned.")

    answer = input(
        "Do you enter the village or investigate the nearby river? "
    ).lower()

    if answer == "village":
        print("You enter the village.")
        print("You find an old house with a light coming from inside.")

        answer = input(
            "Do you knock on the door or sneak around the back? "
        ).lower()

        if answer == "knock":
            print("You knock on the door.")
            print("An old woman opens it.")

            answer = input(
                "She offers you food. Do you accept it or refuse? "
            ).lower()

            if answer == "accept":
                print("You accept the food.")
                print("The woman reveals that she is a powerful wizard.")
                print("She gives you a magical map leading out of the forest.")
                print("You safely escape the Lost Kingdom.")
                print("YOU WIN!")

            elif answer == "refuse":
                print("You refuse the food.")
                print("The woman becomes angry and turns you into a frog.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        elif answer == "back":
            print("You sneak around the back of the house.")
            print("You find a hidden door leading underground.")

            answer = input(
                "Do you enter the tunnel or return to the main road? "
            ).lower()

            if answer == "tunnel":
                print("You enter the underground tunnel.")
                print("You discover an ancient library.")
                print("You find a book describing the entire Lost Kingdom.")
                print("You now know the secrets of the kingdom.")
                print("YOU WIN!")

            elif answer == "road":
                print("You return to the main road.")
                print("A group of bandits spots you and takes everything you have.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        else:
            print("Not a valid option. You lose.")

    elif answer == "river":
        print("You walk toward the river.")
        print("You notice a small boat tied to the shore.")

        answer = input(
            "Do you take the boat or follow the river on foot? "
        ).lower()

        if answer == "boat":
            print("You take the boat across the river.")
            print("Halfway across, the river becomes extremely rough.")

            answer = input(
                "Do you keep going or turn back? "
            ).lower()

            if answer == "keep going":
                print("You hold on and manage to reach the other side.")
                print("You discover a peaceful village.")
                print("The villagers welcome you as a hero.")
                print("YOU WIN!")

            elif answer == "turn back":
                print("You turn the boat around.")
                print("A giant wave flips the boat over.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        elif answer == "walk":
            print("You follow the river on foot.")
            print("You find a strange golden key beside a tree.")

            answer = input(
                "Do you take the key or leave it? "
            ).lower()

            if answer == "take":
                print("You take the key.")
                print("You notice a small locked door behind the tree.")
                print("The key fits perfectly.")
                print("Behind the door is a room filled with treasure.")
                print("You found the legendary treasure!")
                print("YOU WIN!")

            elif answer == "leave":
                print("You leave the key behind.")
                print("You continue walking until the river disappears.")
                print("You become completely lost.")
                print("You lose!")

            else:
                print("Not a valid option. You lose.")

        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing,", name + "!")
