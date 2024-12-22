import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)

user_cards = [random.choice(cards), random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]

print(f"User cards: {user_cards}")
print(f"Dealer cards: {dealer_cards}")

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)

if user_score == 21 and len(user_cards) == 2:
    print("Blackjack! You win!")
elif dealer_score == 21 and len(dealer_cards) == 2:
    print("Dealer has Blackjack! You lose!")
else:
    print(f"User score: {user_score}")
    print(f"Dealer score: {dealer_score}")

    if user_score > 21:
        print("Bust! You lose!")
    elif dealer_score > 21:
        print("Dealer busts! You win!")
    elif user_score == dealer_score:
        print("Draw!")
    elif user_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")