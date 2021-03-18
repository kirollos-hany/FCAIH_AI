from ksproblem import KSProblem
from swarm import Swarm
from uksproblem import UKSProblem

unbounded_type = 1
bounded_type = 2

flag = 1

while flag == 1:
    print("Solving Knapsack Problem Using Particle Swarm Optimization")
    num_items = int(input("Enter number of items:"))
    capacity = int(input("Enter the capacity of the knapsack:"))
    print("Choose problem type from below:")
    print("1-Unbounded Knapsack Problem")
    print("2-(1-0) Knapsack Problem")

    problem_type = int(input())

    ks_problem = KSProblem(num_items, capacity)

    if problem_type == unbounded_type:
        # unbounded knapsack problem
        ks_problem = UKSProblem(num_items, capacity)
        ks_problem.input_vals()
        ks_problem.input_weights()
        

    elif problem_type == bounded_type:
        # 1-0 knapsack problem
        ks_problem.input_vals()
        ks_problem.input_weights()
        

    else:
        print("Invalid choice..try again")
        continue

    particle_swarm = Swarm(
        2**num_items, ks_problem.fit_func, 3 * (2 ** num_items))

    found_sol = particle_swarm.pso(100)

    ks_problem.output_solution(found_sol)

    flag = int(input("Enter 1 to continue or any number to exit\n"))
