print("Welcome to Rock, Paper, Scissors!")
print("")
print("E P I C  ✊ & ✋ & ✌  B A T T L E")
print("")

# Initialize player scores
player_one_score = 0
player_two_score = 0

while True:
    print("")
    print("Select your move (R, P, or S)")
    print("")

    player_one = input("Player One: ")
    print("")
    player_two = input("Player Two: ")
    print("")

    if player_one == player_two:
        print("T I E")
    elif player_one == "P" and player_two == "R":
        print("Player One Wins")
        player_one_score += 1
    elif player_one == "R" and player_two == "P":
        print("Player Two Wins")
        player_two_score += 1
    elif player_one == "S" and player_two == "P":
        print("Player One Wins")
        player_one_score += 1
    elif player_one == "P" and player_two == "S":
        print("Player Two Wins")
        player_two_score += 1
    elif player_one == "R" and player_two == "S":
        print("Player One Wins")
        player_one_score += 1
    elif player_one == "S" and player_two == "R":
        print("Player Two Wins")
        player_two_score += 1

    print("")
    print("Player One Score:", player_one_score)
    print("")
    print("Player Two Score:", player_two_score)
    print("")
  
    # Check if a player has reached three points
    if player_one_score == 3 or player_two_score == 3:
        print("G A M E   O V E R")
        player_one_score = 0  # Reset scores for the next game
        player_two_score = 0
        continue  # Restart the game

    # If no player has reached three points, continue with the next round
