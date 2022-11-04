import random
from utils.cards import cards as cards_img
import os

def cls():
    '''clear the screen'''
    os.system('cls' if os.name=='nt' else 'clear')

def card_to_img(num):
    '''convert the number to an ascii card, with
    random suit(hearts, diamonds, clubs and spades), but
    with identical value in the game'''
    if num == 11:
        return random.choice(cards_img[0:3])
    elif num == 10:
        return random.choice(cards_img[36::])
    elif num == 9:
        return random.choice(cards_img[32:36])
    elif num == 8:
        return random.choice(cards_img[28:32])
    elif num == 7:
        return random.choice(cards_img[24:28])
    elif num == 6:
        return random.choice(cards_img[20:24])
    elif num == 5:
        return random.choice(cards_img[16:20])
    elif num == 4:
        return random.choice(cards_img[12:16])
    elif num == 3:
        return random.choice(cards_img[8:12])
    elif num == 2:
        return random.choice(cards_img[4:8])

def deal_card():
    '''deals a new card in the game'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and 
    return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    '''Compare user and computer score to see
    who won the game.'''
    if user_score > 21 and computer_score > 21:
        return 'You went over 21. You lose.'
    elif user_score == computer_score:
        return 'Its a draw!'
    elif user_score == 0:
        return 'Thats a blackjack! You won !'
    elif computer_score == 0:
        return 'The dealer got a blackjack. you lose'
    elif user_score > 21:
        return 'You went over 21. You lose.'
    elif computer_score > 21:
        return 'The dealer went over 21. You won !'
    elif user_score > computer_score:
        return 'You won!'
    else:
        return 'You lose.'