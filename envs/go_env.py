import gym
from gym.spaces import Discrete, Box
from gym.utils import seeding
import numpy as np


class GoEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = Box(low=0, high=1, dtype=np.int)
        self.action_space = Discrete(n=1)

        self.seed()

    def reset(self):
        pass

    def step(self, action):
        pass

    def close(self):
        pass

    def render(self, mode='human'):
        pass

    def seed(self, seed=None):
        self.np_random, seed1 = seeding.np_random(seed)
        seed2 = seeding.hash_seed(seed1 + 1) % 2 ** 31
        return [seed1, seed2]