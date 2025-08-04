import numpy as np


class Fibonacci:

    @staticmethod
    def get_fibonacci(k):
        golden_ratio = (1 + np.sqrt(5)) / 2
        return int(np.round((golden_ratio ** k + (1 - golden_ratio) ** k) / np.sqrt(5)))

    @staticmethod
    def max_fibonacci(num):
        count = 0
        while Fibonacci.get_fibonacci(count + 2) <= num:
            count += 1
        return count

    @staticmethod
    def num_chips(state):
        num_chips = 0
        stack_list = state.get_stack_list()
        for stack_num in len(stack_list):
            num_chips += stack_list[stack_num] * \
                Fibonacci.get_fibonacci(stack_num + 2)
        return num_chips

    @staticmethod
    def get_terminal_stacks(num):
        num_stacks = Fibonacci.max_fibonacci(num)
        stack_list = np.zeros(num_stacks, dtype=int)
        stack_list[num_stacks - 1] = 1
        decreasing_num = num - \
            Fibonacci.get_fibonacci(num_stacks + 1)
        while decreasing_num > 0:
            next_index = Fibonacci.max_fibonacci(decreasing_num) - 1
            stack_list[next_index] = 1
            decreasing_num = decreasing_num - \
                Fibonacci.get_fibonacci(next_index + 2)
        return stack_list
