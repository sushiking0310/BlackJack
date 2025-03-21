import random

# ASCII Art for logo (you can add one)
logo = '''
Blackjack Game
'''

cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
         '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Function to calculate score with Ace handling
def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score > 21:
        card_list[card_list.index(11)] = 1  # Convert Ace from 11 to 1
        score = sum(card_list)
    return score

# Deal initial cards
user_cards = [cards[random.choice(list(cards.keys()))] for _ in range(2)]
dealer_cards = [cards[random.choice(list(cards.keys()))]]

print("Your hand:", user_cards)
print("Dealer's hand:", dealer_cards)

# User's turn
while True:
    response = input("Type 'y' to hit, 'n' to stand: ").lower()
    if response == 'y':
        user_cards.append(cards[random.choice(list(cards.keys()))])
        print("Your hand:", user_cards)
        if calculate_score(user_cards) > 21:
            print("BUSTED! You lose.")
            break
    else:
        break

# Dealer's turn (only if player hasn't busted)
if calculate_score(user_cards) <= 21:
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(cards[random.choice(list(cards.keys()))])
        print("Dealer's hand:", dealer_cards)

    # Final results
    user_total = calculate_score(user_cards)
    dealer_total = calculate_score(dealer_cards)
    
    print(f"Your final hand: {user_cards} (Total: {user_total})")
    print(f"Dealer's final hand: {dealer_cards} (Total: {dealer_total})")

    if dealer_total > 21:
        print("Dealer BUSTED! You win!")
    elif user_total > dealer_total:
        print("YOU WIN!")
    elif user_total < dealer_total:
        print("Dealer wins!")
    else:
        print("PUSH (It's a tie).")
