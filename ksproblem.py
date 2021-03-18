import itertools


class KSProblem:
    def __init__(self, num_items, capacity):
        self.vals = [0] * num_items
        self.weights = [0] * num_items
        self.capacity = capacity
        self.search_space = [
            list(i) for i in itertools.product([0, 1], repeat=num_items)]
        self.solution = 0

    def fit_func(self, position, print_eval_flag=True):
        total_val = 0
        total_weight = 0
        for i in range(len(self.vals)):

            if self.search_space[position][i] == 1:
                total_val += self.vals[i]
                total_weight += self.weights[i]
        if print_eval_flag:
            print("----------------------")
            print(f"evaluation of solution no.{position}")
            print(f"total weight: {total_weight} total_value: {total_val}")
            print("----------------------")

        if total_weight <= self.capacity:
            return total_val
        else:
            return 0

    def output_solution(self, position):
        optimal_val = self.fit_func(position, False)
        print(f"PSO found solution of optimal value: {optimal_val}")
        items = []
        for i in range(len(self.search_space[position])):
            if(self.search_space[position][i] == 1):
                items.append(i+1)
        print("Items to store in knapsack:")
        for i in range(len(items)):
            print(f"{items[i]}, ", end=" ")

    def input_vals(self):
        for i in range(len(self.vals)):
            self.vals[i] = int(
                input(f"Input (Integer) value of item no.{i+1}:"))

    def input_weights(self):
        for i in range(len(self.weights)):
            self.weights[i] = int(
                input(f"Input (Integer) weight of item no.{i+1}:"))
