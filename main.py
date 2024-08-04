import secrets
import os


def create_deck() -> list:
    suits: list = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks: list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck: list = []

    for i in range(52):
        suit = suits[i // len(ranks)]
        rank = ranks[i % len(ranks)]
        deck.append(f"{rank} of {suit}")

    return deck


def shuffle(deck: list) -> list:
    return sorted(deck, key=lambda _: secrets.randbelow(100))


def getplayers() -> int:
    while True:
        try:
            num_players = int(input("Enter the number of players (1-8): "))
            if 1 <= num_players <= 8:
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

    return num_players


def deal_cards(num_players: int, shuffled_deck: list):
    community_cards = []
    player_cards = [[] for _ in range(num_players)]
    for _ in range(2):
        for player in player_cards:
            player.append(shuffled_deck.pop())

    shuffled_deck.pop()

    for _ in range(5):
        community_cards.append(shuffled_deck.pop())

    print(f"Community Cards: {community_cards}")


    for i, cards in enumerate(player_cards, start=1):
        print(f"Player {i}: {cards}")


def output() -> None:
    return NotImplementedError


def main():
    deck: list = create_deck()
    shuffled_deck: list = shuffle(deck)

    numPlayers: int = getplayers()
    deal_cards(numPlayers, shuffled_deck)

    # print("\n".join(shuffled_deck))


if __name__ == "__main__":
    main()
