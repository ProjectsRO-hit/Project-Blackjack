import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

user_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]

print(f"User cards: {user_cards}")
print(f"Dealer cards: {dealer_cards}")

