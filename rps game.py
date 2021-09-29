while True:
    player1 = input("Player1 Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    player2 = input("Player2 Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    print(f"\nplayer1 chose {player1}, player2 chose {player2}.\n")

    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Rock smashes scissors! player1 wins!")
        else:
            print("Paper covers rock! player2 wins.")
    elif player1 == "paper":
        if player2 == "rock":
            print("Paper covers rock! player1 win!")
        else:
            print("Scissors cuts paper! player2 wins.")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Scissors cuts paper! player1 wins!")
        else:
            print("Rock smashes scissors! player2 wins.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break