import secrets


def create_deck() -> list:
    suits: list = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks: list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck: list = []

    for i in range(52):
        suit = suits[i // len(ranks)]
        rank = ranks[i % len(ranks)]
        deck.append(f"{rank} of {suit}")

    return deck


def getplayers() -> list:
    while True:
        try:
            num_players = int(input("Enter the number of players (1-8): "))
            if 1 <= num_players <= 8:
                break
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

    return num_players


def deal_cards(num_players: int):

    player_cards = [[] for _ in range(num_players)]


def output() -> None:
    return NotImplementedError


def main():
    deck = create_deck()
    shuffled_deck = sorted(deck, key=lambda _: secrets.randbelow(100))

    numPlayers = getplayers()
    print(numPlayers)
    # print("\n".join(shuffled_deck))


if __name__ == "__main__":
    main()
