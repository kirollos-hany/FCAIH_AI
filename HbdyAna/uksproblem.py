from ksproblem import KSProblem


class UKSProblem(KSProblem):

    def fit_func(self, position):
        total_val = 0
        total_weight = 0
        for i in range(len(self.vals)):
            print(f"evaluating solution no.{position}")
            if self.search_space[position][i] == 1:
                total_val += self.vals[i]
                total_weight += self.weights[i]
        print(f"total val before if statement: {total_val}")
        if total_weight != 0 and self.capacity % total_weight == 0:
            total_val = total_val * (self.capacity / total_weight)
            total_weight = total_weight * (self.capacity / total_weight)
            print(f"total val inside if statement: {total_val}")
        print(f"total weight: {total_weight} total_val: {total_val}")
        if total_weight <= self.capacity:
            return total_val
        else:
            return 0


