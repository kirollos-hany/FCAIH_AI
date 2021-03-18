from particle import Particle
import random


class Swarm:
    def __init__(self, bound, fit_func, num_particles):
        self.particles = []
        self.global_best = 0
        self.fit_func = fit_func
        for i in range(num_particles):
            random_pos = random.randint(0, bound - 1)
            random_vel = random.randint(1, bound - 1)
            new_particle = Particle(random_pos, random_vel, bound)
            self.particles.append(new_particle)
            if self.fit_func(self.global_best) < self.fit_func(self.particles[i].position):
                self.global_best = self.particles[i].position

    def pso(self, iterations):
        for i in range(iterations):
            print("**********************************\n")
            print(f"PSO iteration no.{i}")
            for j in range(len(self.particles)):
                self.particles[j].update_vel(global_best=self.global_best)
                self.particles[j].update_pos()
                if self.fit_func(self.particles[j].local_best) < self.fit_func(self.particles[j].position):
                    self.particles[j].update_local_best()
                if self.fit_func(self.particles[j].position) > self.fit_func(self.global_best):
                    self.global_best = self.particles[j].position
            print("**********************************\n")
        return self.global_best
