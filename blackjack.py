import random
import art
import os

print(art.logo)

def draw_card():
    """Draws a random card. Ace (11), 2-10, Jack (10), Queen (10), King (10)."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of a hand. Adjusts Ace value if score exceeds 21."""
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def blackjack_game():
    while True:
        clear_screen()
        print("Welcome to Blackjack!\n")
        
        # Initial card draws
        user_cards = [draw_card(), draw_card()]
        computer_cards = [draw_card(), draw_card()]
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check for blackjack
        if user_score == 21:
            print("You have a Blackjack! You win!")
        elif computer_score == 21:
            print("Computer has a Blackjack! You lose.")
        else:
            # User's turn
            while user_score < 21:
                should_continue = input("Do you want to draw another card? Type 'yes' or 'no': ").lower()
                if should_continue == 'yes':
                    user_cards.append(draw_card())
                    user_score = calculate_score(user_cards)
                    print(f"Your cards: {user_cards}, current score: {user_score}")
                else:
                    break
            
            if user_score > 21:
                print("You went over 21. You lose.")
            else:
                # Computer's turn
                while computer_score < 17:
                    computer_cards.append(draw_card())
                    computer_score = calculate_score(computer_cards)
                
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                
                # Determine winner
                if computer_score > 21 or user_score > computer_score:
                    print("You win!")
                elif user_score == computer_score:
                    print("It's a draw!")
                else:
                    print("You lose!")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

blackjack_game()
