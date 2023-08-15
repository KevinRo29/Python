class GameState:
    def __init__(self):
        self.player_name = ""
        self.story_progress = 0

    def advance_story(self, choice):
        if self.story_progress == 0:
            if choice == 1:
                self.story_progress = 1
            elif choice == 2:
                self.story_progress = 2
        elif self.story_progress == 1:
            if choice == 1:
                self.story_progress = 3
            elif choice == 2:
                self.story_progress = 4
        elif self.story_progress == 2:
            if choice == 1:
                self.story_progress = 5
            elif choice == 2:
                self.story_progress = 6
        elif self.story_progress == 5:
            if choice == 1:
                self.story_progress = 7
            elif choice == 2:
                self.story_progress = 8

    def display_current_scene(self):
        if self.story_progress == 0:
            print("You find yourself in a mysterious forest.")
            print("A path leads to the left, and a river to the right.")
            print("What do you do?")
            print("1. Take the left path.")
            print("2. Follow the river.")
        elif self.story_progress == 1:
            print("You venture down the left path.")
            print("You come across a clearing with a cabin.")
            print("Smoke rises from the chimney. What will you do?")
            print("1. Knock on the door.")
            print("2. Continue on your path.")
        elif self.story_progress == 2:
            print("You decide to follow the riverbank.")
            print("As you walk, you spot a hidden cave.")
            print("A mysterious light emanates from within. What's your choice?")
            print("1. Enter the cave.")
            print("2. Keep walking along the river.")
        elif self.story_progress == 3:
            print("You knock on the cabin's door.")
            print("An old hermit answers and welcomes you inside.")
            print("He offers you a warm meal and shelter.")
            print("You decide to stay for the night.")
        elif self.story_progress == 4:
            print("You continue on your path, ignoring the cabin.")
            print("As night falls, you realize you're lost in the forest.")
            print("The howls of wolves echo through the trees.")
            print("You struggle to find a safe place to rest.")
        elif self.story_progress == 5:
            print("You enter the cave and discover a hidden treasure hoard.")
            print("Your journey has been rewarded!")
        elif self.story_progress == 6:
            print("You continue walking along the riverbank.")
            print("Eventually, you stumble upon a friendly village.")
            print("The villagers welcome you with open arms.")
            print("You've found a new home and a new beginning.")

def get_player_choice():
    choice = int(input("Enter your choice: "))
    return choice

def main():
    game_state = GameState()

    print("Welcome to the Interactive Text-Based Game!")
    game_state.player_name = input("What's your name? ")

    while game_state.story_progress not in [3, 4, 7, 8]:
        game_state.display_current_scene()
        player_choice = get_player_choice()
        game_state.advance_story(player_choice)

    if game_state.story_progress == 3:
        print("Congratulations, " + game_state.player_name + "! You've found shelter and companionship.")
    elif game_state.story_progress == 4:
        print("Unfortunately, " + game_state.player_name + ", your journey ends here.")
    elif game_state.story_progress == 7:
        print("Congratulations, " + game_state.player_name + "! You've found a hidden treasure.")
    elif game_state.story_progress == 8:
        print("Congratulations, " + game_state.player_name + "! You've found a new home and a new beginning.")

if __name__ == "__main__":
    main()
