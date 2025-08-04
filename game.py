import numpy as np
from fibonacci import Fibonacci
from state import State


class Game:
    # A deterministic Zeckendorf game with num_chips starting at state.
    def __init__(self, num_chips, strat1, strat2, initial_state=None):
        self.num_chips = num_chips
        self.strat_list = [strat1, strat2]
        self.terminal_state = State(Fibonacci.get_terminal_stacks(num_chips))
        if initial_state == None:
            stack_list = np.zeros(
                Fibonacci.max_fibonacci(num_chips), dtype=int)
            stack_list[0] = num_chips
            self.initial_state = State(stack_list)
        else:
            self.initial_state = initial_state

    def play(self, state, move, kind):
        new_stack = state.get_stack_list().copy()
        if kind == "combo":
            if move == 0:
                new_stack[0] -= 2
                new_stack[1] += 1
            else:
                new_stack[move] -= 1
                new_stack[move - 1] -= 1
                new_stack[move + 1] += 1
        else:  # i.e., kind == "split"
            if move == 1:
                new_stack[1] -= 2
                new_stack[0] += 1
                new_stack[2] += 1
            else:
                new_stack[move] -= 2
                new_stack[move - 2] += 1
                new_stack[move + 1] += 1
        return State(new_stack)

    # Never called on the terminal state
    def strat_play(self, state, strat):
        splits = state.get_next_splits()
        combos = state.get_next_combos()
        if strat == "ss":
            if len(splits) > 0:
                return self.play(state, splits[0], "split")
            else:
                return self.play(state, combos[0], "combo")
        elif strat == "sl":
            if len(splits) > 0:
                return self.play(state, splits[-1], "split")
            else:
                return self.play(state, combos[-1], "combo")
        elif strat == "cs":
            if len(combos) > 0:
                return self.play(state, combos[0], "combo")
            else:
                return self.play(state, splits[0], "split")
        else:  # strat == "cl"
            if len(combos) > 0:
                return self.play(state, combos[-1], "combo")
            else:
                return self.play(state, splits[-1], "split")

    def find_winner_general(self, state, player):
        if state.is_terminal():
            return 3 - player
        else:
            return self.find_winner_general(self.strat_play(state, self.strat_list[player - 1]), 3 - player)

    def find_winner(self):
        return self.find_winner_general(self.initial_state, 1)

    # Getter methods
    def get_num_chips(self):
        return self.num_chips

    def get_initial_state(self):
        return self.initial_state

    def get_terminal_state(self):
        return self.terminal_state

    def get_num_summands(self):
        return np.sum(self.terminal_state.get_stack_list())

    def get_strat1(self):
        return self.strat_list[0]

    def get_strat2(self):
        return self.strat_list[1]
