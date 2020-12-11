import random
import math


class Particle:
    def __init__(self, position, velocity, bound):
        self.position = position
        self.velocity = velocity
        self.local_best = position
        self.upper_bound = bound
        self.inertia_weight = 0.7
        self.indiv_cog = random.random()
        self.social_cog = random.random()

    def update_pos(self):
        self.position = math.floor(
            (self.position + self.velocity)) % self.upper_bound

    def update_vel(self, global_best):
        self.velocity = (self.velocity * self.inertia_weight) + \
            (self.indiv_cog * (self.local_best - self.position))
        + (self.social_cog * (global_best - self.position))

    def update_local_best(self):
        self.local_best = self.position
