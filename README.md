# 🃏 Blackjack Game 🃏

Welcome to the **Blackjack Game**! This is a Python-based card game where you can test your skills against the computer dealer and aim to get a hand closer to 21 without going over. Will you score a **Blackjack** and win?

## 🎨 Game Logo

```plaintext
logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/  
'''
```

## 🎮 How to Play
1. Objective: Get your hand's total as close to 21 as possible without exceeding it.
2. Blackjack: If your first two cards total 21, it’s a Blackjack, and you win automatically unless the dealer also has a Blackjack.
3. Hit or Stand:
  - Type 'hit' to draw another card.
  - Type 'stand' to end your turn and let the dealer play.
  - The dealer must keep drawing until reaching at least 17. Whoever is closest to 21 without going over wins!

## 🛠️ Features
  - Random Card Drawing: Cards are randomly chosen from a deck each time you play.
  - Automatic Blackjack Check: If you hit 21 with your first two cards, it’s automatically a Blackjack.
  - Dealer Logic: The dealer draws cards until their total score is 17 or higher.

## 🔧 Code Overview
Functions
  - dealCard(): Draws a random card from the deck.
  - calculateScore(): Calculates the score of a hand. Aces are adjusted as needed (1 or 11) to avoid busting.
  - compare(): Compares the user’s score to the computer’s score to determine the game outcome.
  - playBlackJack(): Main function that manages the game, taking player input to hit or stand, and handling the dealer’s turn.

## Sample Code Snippet
```python
from art import logo
import random

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Additional functions: calculateScore(), compare(), and playBlackJack()
```

## 🔄 How to Run the Game
1. Ensure you have Python 3.x installed.
2. Run the script:
```bash
python main.py
```

## 📊 Scoring System
- Blackjack (21 on first two cards): Automatic win unless the dealer also has Blackjack.
- Bust (> 21): Automatic loss.
- Closest to 21: The player with a score closer to 21 wins the round.

## 🤝 Contributing
Feel free to suggest new features or improve existing ones by submitting a pull request. Let's make this game even more fun!



Enjoy the game, and may the odds be in your favor! 🎉

