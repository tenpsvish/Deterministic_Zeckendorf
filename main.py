import pandas as pd
from game import Game

limit = int(input("Maximum N: "))
strat1 = input("Player 1 Strategy (ss/sl/cs/cl): ")
strat2 = input("Player 2 Strategy (ss/sl/cs/cl): ")
winners = []
terminal_states = []
num_summands = []

for num_chips in range(1, limit):
    game = Game(num_chips, strat1, strat2)
    terminal_states.append(game.get_terminal_state().get_stack_list())
    num_summands.append(game.get_num_summands())
    winners.append(game.find_winner())

table_data = {"N": range(1, limit),
              "Winner": winners,
              "Number of Summands": num_summands,
              "Terminal States": terminal_states
              }

table = pd.DataFrame(table_data)
table.to_csv("output.csv", index=False, encoding="utf-8")
print(
    f"Data for the deterministic game {strat1} vs {strat2} for N upto {limit} is now available in output.csv")
