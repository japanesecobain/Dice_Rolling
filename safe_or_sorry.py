def main():
    '''Aoi Araki'''

    from die import Die
    from player import Player
    import random

    num_players = int(input("Enter the number of players (2 or more): "))
    while num_players < 2:
        num_players = int(input("Please enter at least 2 players: "))

    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(Player(name))

    random.shuffle(players)
    print("\nPlayer order:")
    for i, player in enumerate(players):
        print(f"{i+1}. {player.name}")

    safe_die = Die(6)
    risky_die = Die(12)

    game_over = False
    while not game_over:
        for player in players:
            if player.skip_turn:
                print(f"\n{player.name}, you are skipping this turn.")
                player.skip_turn = False
                continue

            print(f"\n{player.name}'s turn. Current score: {player.score}")
            print("Choose an option:")
            print("1: Roll the safe die")
            print("2: Roll the risky die")
            print("3: Choose the minimum value of the safe die and lose next turn")
            print("4: Choose the minimum value of the risky die and lose next turn")
            choice = input("Enter your choice (1-4): ")
            while choice not in ['1', '2', '3', '4']:
                choice = input("Invalid choice. Enter 1, 2, 3, or 4: ")

            if choice == '1':
                value = safe_die.roll()
                print(f"You rolled a {safe_die.current_face} with the safe die.")
                player.update_score(value)
            elif choice == '2':
                value = risky_die.roll()
                if risky_die.current_face <= 6:
                    print(f"You rolled a {risky_die.current_face} with the risky die. Subtracting from your score.")
                else:
                    print(f"You rolled a {risky_die.current_face} with the risky die. Adding to your score.")
                player.update_score(value)
            elif choice == '3':
                value = 1 
                print(f"You took the minimum value ({value}) of the safe die and will skip your next turn.")
                player.update_score(value)
                player.skip_turn = True
            elif choice == '4':
                value = -1  
                print(f"You took the minimum value ({-value}) of the risky die and will skip your next turn.")
                player.update_score(value)
                player.skip_turn = True

            print(f"{player.name}'s new score: {player.score}")

            if player.score == 30:
                print(f"\nCongratulations {player.name}! You have reached 30 points and won the game!")
                game_over = True
                break
            elif player.score > 30:
                print(f"{player.name}, your score has exceeded 30. Your score will reset to 0.")
                player.score = 0
            elif player.score < 0:
                print(f"{player.name}, your score has dropped below 0. Your score will reset to 0.")
                player.score = 0

    print("\nGame Over.")

main()

#Abstraction
#Inheritance
#Encapsulation
#Polymorphism