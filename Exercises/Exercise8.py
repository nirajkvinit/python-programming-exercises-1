# Making a rock-paper-scissors game
import time

game = 1

while game == 1:
    winner = 0

    # Player inputs

    player1_ready = 0

    while(player1_ready == 0):

        player1 = input("\nPlayer 1 choose one (rock, paper, scissors): ").lower()

        if(player1.lower() == "rock" or player1.lower() == "paper" or player1.lower() == "scissors"):
            break

    player2_ready = 0

    while (player1_ready == 0):

        player2 = input("\nPlayer 2 choose one (rock, paper, scissors): ").lower()

        if (player2.lower() == "rock" or player2.lower() == "paper" or player2.lower() == "scissors"):
            break

    time.sleep(2)
    print("\nPlayer one chooses %s!" % player1)
    time.sleep(2)
    print("\nPlayer two chooses %s!" % player2)
    time.sleep(2)

    print("\nThe battle starts!")

    for x in range(5):
        time.sleep(1)
        print("\n...")


    def battle(a, b):
        global winner
        if(a == "paper"):
            if b == "paper":
                winner = 0
            elif b == "rock":
                winner = 1
            else:
                winner = 2
        if (a == "rock"):
            if b == "rock":
                winner = 0
            elif b == "scissors":
                winner = 1
            else:
                winner = 2
        if (a == "scissors"):
            if b == "scissors":
                winner = 0
            elif b == "paper":
                winner = 1
            else:
                winner = 2

        return winner

    time.sleep(2)
    result = battle(player1, player2)
    if result == 0:
        print("\nLadies and gentlemen, we don't have a winner..")
    else:
        print("\nLadies and gentlemen, we have a winner..")
    time.sleep(2)



    if result == 0:
        print("\nIt's a tie!")
    elif result == 1:
        print("\nThe winner is player 1 with %s!" % player1)
    else:
        print("\nThe winner is player 2 with %s!" % player2)

    time.sleep(2)

    print("\nThank you for participating in this great event.")

    new_game = input("Would you like to start a new fight (y/n): ")

    if new_game == "y":
        continue
    else:
        print("Goodbye!")
        game = 0

