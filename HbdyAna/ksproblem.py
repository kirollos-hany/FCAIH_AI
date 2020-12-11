import itertools


class KSProblem:
    def __init__(self, num_items, capacity):
        self.vals = [0] * num_items
        self.weights = [0] * num_items
        self.capacity = capacity
        self.search_space = [
            list(i) for i in itertools.product([0, 1], repeat=num_items)]
        self.solution = 0

    def fit_func(self, position):
        total_val = 0
        total_weight = 0
        for i in range(len(self.vals)):
            print(f"evaluating solution no.{position}")
            if self.search_space[position][i] == 1:
                total_val += self.vals[i]
                total_weight += self.weights[i]
        print(f"total weight: {total_weight} total_val: {total_val}")
        if total_weight <= self.capacity:
            return total_val
        else:
            return 0

    def input_vals(self):
        for i in range(len(self.vals)):
            self.vals[i] = int(
                input(f"Input (Integer) value of item no.{i+1}:"))

    def input_weights(self):
        for i in range(len(self.weights)):
            self.weights[i] = int(
                input(f"Input (Integer) weight of item no.{i+1}:"))
