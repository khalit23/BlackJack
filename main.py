import random
from sticker import logo, winner, loser, draw


def hand_out_cards():
    """add a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card_picked_from_deck = random.choice(cards)
    return card_picked_from_deck


def calculate_total(cards):
    """Calculates the sum of all the cards in hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return 21

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def outcomes_of_game(player_score, cpu_score):
    if player_score > 21 and cpu_score > 21:
        print(loser)
        return "You went over. You lose 😤"

    if player_score == cpu_score:
        print(draw)
        return "You have the same score! It's a draw!"

    elif cpu_score == 21:
        print(loser)
        return "CPU has a Blackjack! You've lost"

    elif player_score == 21:
        print(winner)
        return "You've got a Blackjack! You win! "

    elif player_score > 21:
        print(loser)
        return "You've gone over 21! You've gone bust! Game over"

    elif cpu_score > 21:
        print(winner)
        return "CPU went over 21! You win "

    elif player_score > cpu_score:
        print(winner)
        return "You win"

    else:
        print(loser)
        return "You lose"


def start_game():
    player_cards = []
    cpu_cards = []
    game_over = False

    print(logo)

    for n in range(1, 3):
        player_cards.append(hand_out_cards())
        cpu_cards.append(hand_out_cards())

    while not game_over:

        player_total = calculate_total(player_cards)
        cpu_total = calculate_total(cpu_cards)

        print(f"Your current hand is {player_cards} which gives you a score of {player_total}")
        print(f"The CPU's first card is {cpu_cards[0]}")

        if player_total == 0 or cpu_total == 0 or player_total > 21:
            game_over = True

        else:
            want_more_cards = input("Would you like another card?: Type 'y' or 'n': ")

            if want_more_cards == "y" and player_total < 21:
                player_cards.append(hand_out_cards())
                print(logo)

            else:
                game_over = True

    while cpu_total < 17 and cpu_total != 0:
        cpu_cards.append(hand_out_cards())
        cpu_total = calculate_total(cpu_cards)

    print(outcomes_of_game(player_total, cpu_total))
    print(f"Your final hand is {player_cards} which gives you a score of {player_total}")
    print(f"The CPU's final hand is {cpu_cards} which gives it a score of {cpu_total}")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    start_game()

else:
    print("Maybe next time?")

