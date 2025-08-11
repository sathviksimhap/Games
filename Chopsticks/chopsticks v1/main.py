import art

game_over = False
player_hands = [[1, 1], [1, 1]]

def display(player):

    print("")
    print("Player One : ", art.hands[player[0][0]][player[0][1]])
    print("Player Two : ", art.hands[player[1][0]][player[1][1]])

def player_one_input(player):

    print("Player One\'s Turn")
    player_one_hand = input("Your Hand : Left(l)    Right(r) : ")
    player_two_hand = input("Their Hand : Left(l)    Right(r) : ")

    #Checking for all usable hands
    if ((player_one_hand == 'l' and player[0][0] == 0) or (player_one_hand == 'r' and player[0][1] == 0) or
            (player_two_hand == 'l' and player[1][0] == 0) or (player_two_hand == 'r' and player[1][1] == 0)):
        print("Can\'t use hand as it is out")
        return player_one_input(player)

    #All error cases
    if (player_one_hand != 'l' and player_one_hand != 'r') or (player_two_hand != 'l' and player_two_hand != 'r'):
        print("Invalid Input")
        return player_one_input(player)

    #All valid cases
    if player_one_hand == 'l':

        if player_two_hand == 'l':
            player[1][0] = (player[1][0] + player[0][0]) % 5
            return player

        elif player_two_hand == 'r':
            player[1][1] = (player[1][1] + player[0][0]) % 5
            return player

    elif player_one_hand == 'r':

        if player_two_hand == 'l':
            player[1][0] = (player[1][0] + player[0][1]) % 5
            return player

        elif player_two_hand == 'r':
            player[1][1] = (player[1][1] + player[0][1]) % 5
            return player

def player_two_input(player):

    print(f"Player Two\'s Turn")
    player_two_hand = input("Your Hand : Left(l)    Right(r) : ")
    player_one_hand = input("Their Hand : Left(l)    Right(r) : ")

    # Checking for all usable hands
    if ((player_two_hand == 'l' and player[1][0] == 0) or (player_two_hand == 'r' and player[1][1] == 0) or
            (player_one_hand == 'l' and player[0][0] == 0) or (player_one_hand == 'r' and player[0][1] == 0)):
        print("Can\'t use hand as it is out")
        return player_two_input(player)

    # All error cases
    if (player_one_hand != 'l' and player_one_hand != 'r') or (player_two_hand != 'l' and player_two_hand != 'r'):
        print("Invalid Input")
        return player_two_input(player)

     # All valid cases
    if player_two_hand == 'l':

        if player_one_hand == 'l':
            player[0][0] = (player[0][0] + player[1][0]) % 5
            return player

        elif player_one_hand == 'r':
            player[0][1] = (player[0][1] + player[1][0]) % 5
            return player

    elif player_two_hand == 'r':

        if player_one_hand == 'l':
            player[0][0] = (player[0][0] + player[1][1]) % 5
            return player

        elif player_one_hand == 'r':
            player[0][1] = (player[0][1] + player[1][1]) % 5
            return player

# Main

print("Welcome to the Chopsticks Game!")
display(player_hands)

while not game_over:

    player_hands = player_one_input(player_hands)
    display(player_hands)

    if player_hands[1] == [0,0]:
        print("Player one Wins !")
        game_over = True

    else:

        player_hands = player_two_input(player_hands)
        display(player_hands)

        if player_hands[0] == [0,0]:
            print("Player Two Wins !")
            game_over = True
