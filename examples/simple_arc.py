# simple example: generate a circular arc curve callable
import numpy as np

class ArcCurve:
    def __init__(self, radius=1.0, height=0.0):
        self.radius = radius
        self.height = height

    def eval_point(self, t):
        theta = 2 * np.pi * t
        return np.array([self.radius * np.cos(theta), self.radius * np.sin(theta), self.height * t])

    def eval_derivative(self, t, order=1):
        theta = 2 * np.pi * t
        if order == 1:
            return np.array([-2 * np.pi * self.radius * np.sin(theta), 2 * np.pi * self.radius * np.cos(theta), self.height])
        elif order == 2:
            return np.array([- (2 * np.pi) ** 2 * self.radius * np.cos(theta), - (2 * np.pi) ** 2 * self.radius * np.sin(theta), 0.0])
        return np.array([0.0, 0.0, 0.0])
