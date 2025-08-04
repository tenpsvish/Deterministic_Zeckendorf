import numpy as np


class State:

    # We assume that there is at least one stack,
    # i.e., len(stack_list) >= 1
    def __init__(self, stack_list):
        self.stack_list = stack_list

    def __eq__(self, other):
        if not isinstance(other, State):
            # Does not attempt to compare against other classes
            return NotImplemented
        return np.array_equal(self.stack_list, other.stack_list)

    # This method allows us to create a dictionary of states in the game, storing their children and winning status.
    def __hash__(self):
        return hash(tuple(self.stack_list))

    # def get_next_moves(self):
    #     next_moves = []
    #     for stack_num in range(len(self.stack_list)):
    #         if stack_num == 0 and self.stack_list[0] >= 2:
    #             next_moves.append((0, "combo"))
    #         if stack_num >= 1 and self.stack_list[stack_num] >= 2:
    #             next_moves.append((stack_num, "split"))
    #         if stack_num >= 1 and self.stack_list[stack_num] >= 1 and self.stack_list[stack_num - 1] >= 1:
    #             next_moves.append((stack_num, "combo"))
    #     next_moves.reverse()
    #     return next_moves

    def get_next_combos(self):
        next_combos = []
        for stack_num in range(len(self.stack_list)):
            if stack_num == 0 and self.stack_list[0] >= 2:
                next_combos.append(0)
            elif stack_num >= 1 and self.stack_list[stack_num] >= 1 and self.stack_list[stack_num - 1] >= 1:
                next_combos.append(stack_num)
        return next_combos

    def get_next_splits(self):
        next_splits = []
        for stack_num in range(1, len(self.stack_list)):
            if self.stack_list[stack_num] >= 2:
                next_splits.append(stack_num)
        return next_splits

    def is_terminal(self):
        return len(self.get_next_combos()) + len(self.get_next_splits()) == 0

    # Getter methods
    def get_stack_list(self):
        return self.stack_list
