import art
from brains import Brain

brain = Brain()
game_on = True
player_hands = [[1, 1], [1, 1]]

def display(p_player_hands):

    print("")
    print("Player One : ", art.hands[p_player_hands[0][0]][p_player_hands[0][1]])
    print("Player Two : ", art.hands[p_player_hands[1][0]][p_player_hands[1][1]])

def player_input(player, p_player_hands):

    print(f"Player {player+1}\'s turn")
    hit_or_switch = input("Choose: Hit(h)    Switch(s): ")

    if hit_or_switch == 'h':
        return brain.hit(player, p_player_hands)
    elif hit_or_switch == 's':
        #Checking if switch is possible
        total_fingers = player_hands[player][0] + player_hands[player][1]
        if 1 < total_fingers < 8:
            return brain.switch(player, p_player_hands)
        else:
            print("Cant switch.")
            return brain.hit(player, p_player_hands)
    else:
        print("Invalid Choice")
        return player_input(player, p_player_hands)

# Main
print(art.welcome)
display(player_hands)

while game_on:

    player_hands = player_input(0, player_hands)
    display(player_hands)

    if player_hands[1] == [0,0]:
        print(art.player_one_wins)
        game_on = False
        break

    player_hands = player_input(1, player_hands)
    display(player_hands)

    if player_hands[0] == [0,0]:
        print(art.player_two_wins)
        game_on = False
        break