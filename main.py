
class Player:

    def __init__(self):
        self.knife = False
        self.security_codes = False
        self.computer_terminal = False
        self.molotov_cocktail = False
        self.armor = False
        self.crowbar = False

    def pickup_item(self, room_name):
        if room_name == "Crew Quarters 1":
            if self.knife == False:    
                self.knife = True
                print("You place the knife in your belt.\n")
                return
            else:
                return
        elif room_name == "Crew Quarters 2":
            if self.security_codes == False:    
                self.security_codes = True
                print("You place the security codes in your pocket.\n")
                return
            else:
                return
        elif room_name == "Common Area":
            if self.computer_terminal == False and self.security_codes == True:
                message = ("Taking the slip of paper out of your pocket, you carefully enter\n"
                "in each digit of the security code. As you punch in the last digit,\n"
                "the screen changes and says, 'Access Granted. Airlock controls are\n"
                "unlocked.' You look around; but you do not see an airlock.\n"
                "Perhaps it is somewhere else in the ship?\n")
                print(message)
                self.computer_terminal = True
            elif self.computer_terminal == False and self.security_codes == False:
                print("Perhaps there are security codes located elsewhere on the ship!\n")
            else:
                return
        elif room_name == "Dining Area":
            if self.molotov_cocktail == False:
                message = ("If the Villain is as ferocious as it sounds, you might be able\n"
                "to use this bottle of Vodka as a Molotov Cocktail, you think to yourself,\n"
                "as you put the bottle, cloth, and matches in your backpack.\n")    
                print(message)
                self.molotov_cocktail = True
                if self.crowbar == True:
                    message = ("Now you turn your attention to the hatch where you can still\n"
                    "hear the animal like growling sound coming from. You use the crowbar\n"
                    "you found to open the hatch.\n")
                    print(message)
                return
            else:
                return
        elif room_name == "Storage Room":
            if self.armor == False:
                print("You pick up the body armor and put it on.\n")
                self.armor = True
            else:
                return
        elif room_name == "Engine Room":
            if self.crowbar == False:
                print("You pick up the crowbar and put it in your backpack.\n")
                self.crowbar = True
            else:
                return
        elif room_name == "VILLAIN!":
            if self.knife == True:
                print("You take out the knife, the Reaver takes a swipe at you and knocks the knife out of your hand.\n")
            else:
                print("The Reaver takes a swipe at you, but you don't have anything to use to defend yourself. You are defeated. GAME OVER!!\n")

            if self.armor == True:
                print("Immediately, the Reaver takes another swipe at you. The body armor you are wearing protects you from its attack.\n")
            else:
                print("Immediately, the Reaver takes another swipe at you, but you don't have anything to protect yourself. You are defeated. GAME OVER!!\n")

            if self.molotov_cocktail:
                print("Before the Reaver can attack you again, you light the Molotov cocktail and throw it at the monster, catching it on fire and distracting the monster for a few moments.\n")
            else:
                print("The Reaver attacks again, but you don't have anything else to use to defend yourself. You are defeated. GAME OVER!!\n")

            if self.computer_terminal:
                print("While the Reaver is distracted, you look around and the Airlock controls are right next to you. You immediately press the button to open the Airlock and the Reaver is immediately sucked out into space.  You Win!!\n")
            else:
                print("The Reaver recovers and trains its attention on you. It attacks, but you don't have anything else to use to defend yourself. You are defeated. GAME OVER!!\n")
            
            quit()
        else:
            print("There are no items in this room.\n")
            return
        print("\n")


class Room:

    def __init__(self, name, description = "", directions={}):
        self.name = name
        # The following four values are Room objects
        self.description = description
        self.directions = directions

    
    def look_around(self):
        print("You are in", self.name)
        print("")
        print(self.description)
        print("")
        return


    def add_directions(self, rooms_dict, room_key):
        for key, value in rooms_dict.items():
            if key == room_key:
                self.directions = {key: value}
                return
        print("Cannot add directions. No key found") # error message in case of trouble adding directions
        return
    

    def add_description(self, story_dict, room_name):
        for key, value in story_dict.items():
            if key == room_name:
                self.description = value
                return
        print("Cannot add description. No key found.") # error message in case of trouble adding description
        return


def change_room(current_room, the_player):
    # Initialize variables
    # Calls the global variable end_game to modify it.
    global end_game
    this_room = ""
    room_options = {}
    valid_choice = False
    
    # if player is in VILLAIN! room:
    if current_room.name == "VILLAIN!":
        print(current_room.description)
        print("")
        the_player.pickup_item(current_room.name)
    
    # Extract directions as dictionary from Room object
    working_room = current_room.directions

    # Unpack the various rooms from dictionary value for current room
    for key, value in working_room.items():
        this_room = key
        room_options = value
    # Tell the player what room they are in.
    print("\nYou are currently in", this_room)
    print("")

    # Tell the player what rooms they can travel to.
    for key, value in room_options.items():
        print("To the", key, "is the room:", room_options[key])

    # As long as player enters a valid direction or the word 'quit'
    # They will either travel to the selected room or end the game.
    # Otherwise, they will have to enter a valid choice.
    while not valid_choice:
        print("\nPlease type one of the following:")
        # Options for player to walk to a different room.
        print("1 Walk North.")
        print("2 Walk South.")
        print("3 Walk East")
        print("4 Walk West")
        # Option to Look Around + Pick up any items in room.
        print("5 Look Around")
        # Option for player to quit the game.
        player_choice = (input("To quit, type 'quit': ")).lower()
        print("\n")
        if player_choice == "quit":
            end_game = True
            return current_room
        # If the player chooses "look around" show Room.description (story for current room)
        # and pick up the item in the room, if it exists.
        elif player_choice == "5" or player_choice == "look around":
            current_room.look_around()
            the_player.pickup_item(current_room.name)
            for key, value in room_options.items():
                print("To the", key, "is the room:", room_options[key])
        else:
            if player_choice == '1':
                player_choice = "north"
            elif player_choice == "2":
                player_choice = "south"
            elif player_choice == "3":
                player_choice = "east"
            elif player_choice == "4":
                player_choice = "west"
            for key, value in room_options.items():
                if player_choice == key.lower():
                    next_room = Room(value) # Create new room object for next room.
                    # At this point, as long as the player entered a valid direction,
                    # the next room will be returned to original function call.
                    return next_room
                else:
                    pass
            # If, after comparing player's input to all room options,
            # the input does not match any of the room options, we give the player
            # an error and remind them where they are and which options they need
            # to choose from.
            print("Input is not valid! You are currently in", this_room)
            print("")

            for key, value in room_options.items():
                print("To the", key, "is the room:", room_options[key])


if __name__ == "__main__":

    # Initialize variables
    serenity_rooms = {
        'Cockpit': {'South': 'Corridor'},
        'Crew Quarters 1': {'East': 'Corridor'},
        'Corridor': {'North': 'Cockpit', 'South': 'Common Area', 'East': 'Crew Quarters 2', 'West': 'Crew Quarters 1'},
        'Crew Quarters 2': {'West': 'Corridor'},
        'Common Area': {'North': 'Corridor', 'South': 'Storage Room', 'East': 'Dining Area'},
        'Dining Area': {'South': 'VILLAIN!','West': 'Common Area'},
        'Storage Room': {'North': 'Common Area', 'South': 'Engine Room'},
        'VILLAIN!': {'North': 'Dining Area'},
        'Engine Room': {'North': 'Storage Room'}
    }

    firefly_story = {
        "Cockpit": ("!! ALARM !! You wake up to the deafening sound of an alarm. As you look around, you notice\n"
            "that a bright red light is flashing on an instrument panel, in front of you. You remember that\n"
            "you are in the cockpit of your spaceship, Serenity, a Firefly class ship you have been hired to\n"
            "pilot. You realize there is no power, aside from the faint white emergency light behind you\n"
            "the bright red flashing light, and the loud booming alarm. There is a button near the flashing\n"
            "light that looks like it might turn off the alarm. You decide to press the button.\n"
            "The alarm stops."),
        "Crew Quarters 1": ("The growling sound gets quieter in this room. As you look around, you can see four beds;\n"
            "they are still made and it does not look like anyone has slept here in a while. At the heads of\n"
            "each of the beds are small storage lockers. One of the locker's door is wide open and you find\n"
            "a knife inside."),
        "Corridor": ("You are in a corridor--there is nothing of interest here. You notice a faint white light coming \n"
            "from the emergency light on the wall. !! GROWL !! There is an animal-like growling sound coming from \n"
            "somewhere in the ship! BE ON YOUR GUARD!"),
        "Crew Quarters 2": ("The growling sound gets quieter in this room. As you look around, you can see\n"
            "four beds; they are still made and it does not look like anyone has slept here in a while. At\n"
            "the heads of each of the beds are small storage lockers. You see a small slip of writing paper on\n"
            "one of the beds. As you examine the paper, it reads, 'Security Codes - 8 5 9 7 2 0 1'."),
        "Common Area": ("The animal like growling sound is louder; it sounds like it is coming from the East. You\n"
            "recognize this room as the common area. Along the back wall is a bar with several bottles of liquor,\n"
            "clean glasses, and empty bins designed to hold ice. There are two tables with chairs near the West\n"
            "wall of the room. On the Southern side of the room stands a lone computer terminal. There is a faint\n"
            "light coming from the computer screen. It has power! You approach the computer terminal and there is\n"
            "a message on the screen saying, 'Enter Security Codes _ _ _ _ _ _ _'"),
        "Dining Area": ("The animal like growling sound is much louder in this room!  You look around and notice you are now\n"
            "in the dining room.  There are ovens, stovetops, and a walk-in freezer on the Eastern wall.  In the\n"
            "middle of the room lies a large table with eight chairs evenly spaced on both sides of the table. The\n"
            "animal like growling sound is coming from a loose hatch located on the Southern wall. Out of the corner\n"
            "of your eye, you notice a full bottle of Vodka on one of the countertops."),
        "Storage Room": ("The growling sound gets quieter in this room. You find yourself in a dimly lit storage room.\n"
            "There are several tall shelves in here, mostly filled with heavy-looking boxes.  On one of the nearby\n"
            "shelves, you find some body armor."),
        "VILLAIN!": ("As you enter the last room, you come face-to-face with a large Reaver, that is standing there growling\n"
            "at you. It attacks!"),
        "Engine Room": ("The animal like growling sound is much quieter in this room. You are now in the engine room.\n"
            "The engine, however, is silent and still. Perhaps this is why the ship is on emergency power? Lying on the\n"
            "floor near the engine, you see a crowbar.")
    }

    end_game = False
    alarm_silent = False

    # create the player object
    the_player = Player()
    current_room = Room(name="Cockpit", description="") # create initial room starting with the Cockpit

    # add cockpit directions and description to current_room
    current_room.add_directions(serenity_rooms, current_room.name)
    current_room.add_description(firefly_story, current_room.name)


    print("___________.__                _____.__                _________                           .__  __          ")
    print("\_   _____/|__|______   _____/ ____\  | ___.__. /\   /   _____/ ___________   ____   ____ |__|/  |_ ___.__.")
    print(" |    __)  |  \_  __ \_/ __ \   __\|  |<   |  | \/   \_____  \_/ __ \_  __ \_/ __ \ /    \|  \   __<   |  |")
    print(" |     \   |  ||  | \/\  ___/|  |  |  |_\___  | /\   /        \  ___/|  | \/\  ___/|   |  \  ||  |  \___  |")
    print(" \___  /   |__||__|    \___  >__|  |____/ ____| \/  /_______  /\___  >__|    \___  >___|  /__||__|  / ____|")
    print("     \/                    \/           \/                  \/     \/            \/     \/          \/     ")
    print("\n\n")

    print(current_room.description)

    while not end_game:
        # run function above to change rooms
        current_room = change_room(current_room, the_player)
        # add directions and description to current_room
        current_room.add_directions(serenity_rooms, current_room.name)
        current_room.add_description(firefly_story, current_room.name)

