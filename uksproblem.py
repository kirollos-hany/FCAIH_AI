from ksproblem import KSProblem


class UKSProblem(KSProblem):

    def fit_func(self, position, print_eval_flag = True):
        total_val = 0
        total_weight = 0
        for i in range(len(self.vals)):

            if self.search_space[position][i] == 1:
                total_val += self.vals[i]
                total_weight += self.weights[i]
        if total_weight != 0 and self.capacity % total_weight == 0:
            total_val = total_val * (self.capacity / total_weight)
            total_weight = total_weight * (self.capacity / total_weight)
        if print_eval_flag:
            print("----------------------")
            print(f"evaluating solution no.{position}")
            print(f"total weight: {total_weight} total_value: {total_val}")
            print("----------------------")
        if total_weight <= self.capacity:
            return total_val
        else:
            return 0
