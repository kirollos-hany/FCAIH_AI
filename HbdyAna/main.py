from ksproblem import KSProblem
from swarm import Swarm


print("Solving Knapsack Problem Using Particle Swarm Optimization")

num_items = int(input("Enter number of items:"))

capacity = int(input("Enter the capacity of the knapsack:"))

ks_problem = KSProblem(num_items, capacity)
ks_problem.input_vals()
ks_problem.input_weights()

particle_swarm = Swarm(2**num_items, ks_problem.fit_func, num_items * 2)

found_sol = particle_swarm.pso(1000)

print(f"PSO found solution: {found_sol} of optimal val: {ks_problem.fit_func(found_sol)}")
