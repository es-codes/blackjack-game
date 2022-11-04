from utils.logo import logo
from utils.helper import card_to_img, cls, deal_card, calculate_score, compare
import random

def playing():
    
    user_cards = []
    user_pictures_cards = []
    dealer_cards = []
    dealer_pictures_cards = []
    player_round = False
    
    print(f'{logo}\n')
    print('--------------')
    print ('Welcome!')
    print('--------------')
    
    for _ in range(2):
            user_cards.append(deal_card())
            dealer_cards.append(deal_card())
            user_pictures_cards.append(card_to_img(user_cards[_]))
            dealer_pictures_cards.append(card_to_img(dealer_cards[_]))

    print(f'Here is your hand: {user_pictures_cards[0]}{user_pictures_cards[1]}')
    print(f'Here is the dealer upside card: {dealer_pictures_cards[0]}')

    while not player_round:
        
        if calculate_score(user_cards) == 0 and calculate_score(dealer_cards) == 0:
            print(f'Wow ! You both got blackjacks, its a draw !')
            player_round = True
        elif calculate_score(user_cards) == 0:
            print('You got a blackjack ! You Won !')
            player_round = True
        elif calculate_score(dealer_cards) == 0:
            print('The dealer got a blackjack, you lose !')
            player_round = True
        else:
            user_choice = input('Do you want another card? ("yes" to continue, "no" to stop)  ')
            if user_choice == "yes":
                new_card = deal_card()
                user_cards.append(new_card)
                user_pictures_cards.append(card_to_img(new_card))
                print('Here is your hand: ')
                for card in user_pictures_cards:
                    print(card)
                if calculate_score(user_cards) > 21:
                    print('Ops, You went over 21.')
                    break
            else:
                player_round = True
    
    while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
        new_card2 = deal_card()
        dealer_cards.append(new_card2)
        dealer_pictures_cards.append(card_to_img(new_card2))
    
    
    print('Here is your final hand: ')
    for card in user_pictures_cards:
        print(card)
    
    print('Here is the dealers final hand: ')
    for card in dealer_pictures_cards:
        print(card)
    print('Final result: ')
   
    print(compare(calculate_score(user_cards), calculate_score(dealer_cards)))
    
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no':  ") == "yes":
    cls()
    playing()
                


        
