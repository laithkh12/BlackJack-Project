import random
from art import logo
def dealCard():
    """
    :return:
    random card from the deck
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return  card

def calculateScore(cards):
    """
    Take list of cards and calculate score
    :param cards:
    :return:
    score of the cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Loss, opponent has BlackJack"
    elif u_score == 0:
        return "Win, with a BlackJack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win."
    else:
        return "You lose."

def playBlackJack():
    print(logo)
    userCards = []
    computerCards = []
    computerScore = -1
    userScore = -1
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"Your cards: {userScore}, current score: {userScore}")
        print(f"Computer first card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
            if userShouldDeal == 'hit':
                userCards.append(dealCard())
            elif userShouldDeal == 'stand':
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer final hand: {computerCards}, final score: {computerScore}")
    print(compare(userScore, computerScore))

while input("Do you want to play a game of BlackJack? 'y' or 'n'") == 'y':
    print("\n" * 20)
    playBlackJack()