import art

class Brain:
    def __init__(self):
        self.winner = 0

    def hit(self, player, player_hands):

        if player == 0:opp = 1
        else: opp = 0
        your_hand = input("Choose your hand: Left(l)    Right(r):")
        opp_hand = input ("Choose their hand: Left(l)    Right(r):")

        #INVALID INPUTS
        # All error cases
        if (your_hand != 'l' and your_hand != 'r') or (opp_hand != 'l' and opp_hand != 'r'):
            print("Invalid Input")
            return self.hit(player, player_hands)

        #All usable hands
        if ((your_hand == 'l' and player_hands[player][0] == 0) or (your_hand == 'r' and player_hands[player][1] == 0) or
                (opp_hand == 'l' and player_hands[opp][0] == 0) or (opp_hand == 'r' and player_hands[opp][1] == 0)):
            print("Can\'t use hand as it is out")
            return self.hit(player, player_hands)

        #All valid cases
        if your_hand == 'l':

            if opp_hand == 'l':
                player_hands[opp][0] = (player_hands[opp][0] + player_hands[player][0]) % 5
            else:
                player_hands[opp][1] = (player_hands[opp][1] + player_hands[player][0]) % 5

        else:

            if opp_hand == 'l':
                player_hands[opp][0] = (player_hands[opp][0] + player_hands[player][1]) % 5
            else:
                player_hands[opp][1] = (player_hands[opp][1] + player_hands[player][1]) % 5

        return player_hands

    def switch(self, player, player_hands):

        options = []
        total_fingers = player_hands[player][0] + player_hands[player][1]

        # Generating all valid switch options
        for i in range((total_fingers + 1)):
            left_fingers = i
            right_fingers = total_fingers - i

            if left_fingers != player_hands[player][0] and right_fingers != player_hands[player][1]:
                if left_fingers < 5 and right_fingers < 5:
                    options.append([left_fingers, right_fingers])

        # printing all available options
        print("Your Switch Options are: ")
        for i in range(len(options)):
            print(f"({i}) : {art.hands[options[i][0]][options[i][1]]}")

        # switch option input
        switch_option = int(input("Choose your switch option: "))

        if switch_option > (len(options) - 1):
            print("Invalid Switch Options")
            return self.switch(player, player_hands)
        else:
            player_hands[player] = options[switch_option]
            return player_hands