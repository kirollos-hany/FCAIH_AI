from ksproblem import KSProblem
from swarm import Swarm
from uksproblem import UKSProblem


print("Solving Knapsack Problem Using Particle Swarm Optimization")

num_items = int(input("Enter number of items:"))

capacity = int(input("Enter the capacity of the knapsack:"))
#1-0 knapsack problem
# ks_problem = KSProblem(num_items, capacity)
# ks_problem.input_vals()
# ks_problem.input_weights()
#unbounded knapsack problem
uks_problem = UKSProblem(num_items, capacity)
uks_problem.input_vals()
uks_problem.input_weights()

particle_swarm = Swarm(2**num_items, uks_problem.fit_func, 3 * (2 ** num_items))

found_sol = particle_swarm.pso(100)

print(f"PSO found solution: {found_sol} of optimal val: {uks_problem.fit_func(found_sol)}")


  
