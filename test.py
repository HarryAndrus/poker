# import random
# original_list = [1, 2, 3, 4, 5, 6, 7, 8]
# deck = random.sample(original_list, len(original_list))
# player1 = deck[:2]
# community= deck[2:7]
# hand_result = "Not implemented"
# print(f"Player 1:\n{'\n'.join(map(str, player1))}")
# print(f"Community:\n{'\n'.join(map(str, community))}")
# print(f"You have: {hand_result}")

num_players = 5
players = [[] for _ in range(num_players)]
print(players)