import numpy as np

class RulingCalculator:
    def __init__(self, analyzer, ruling_angle_func=None):
        self.analyzer = analyzer
        self.ruling_angle_func = ruling_angle_func or (lambda i: np.pi / 2)
        self.ruling_vectors = []
        self._compute_rulings()

    def _compute_rulings(self):
        n = len(self.analyzer.points)
        for i in range(n):
            gamma = self.ruling_angle_func(i)
            T = self.analyzer.tangents[i]
            N = self.analyzer.normals[i]
            B = self.analyzer.binormals[i]

            R_base = np.cos(gamma) * T + np.sin(gamma) * N
            # store base vectors for alpha=0
            self.ruling_vectors.append((R_base, R_base))

    def get_ruling_at_deployment(self, alpha):
        deployed = []
        for i in range(len(self.analyzer.points)):
            gamma = self.ruling_angle_func(i)
            T = self.analyzer.tangents[i]
            N = self.analyzer.normals[i]
            B = self.analyzer.binormals[i]

            R_left = (np.cos(gamma) * T + 
                      np.sin(gamma) * np.cos(alpha) * N + 
                      np.sin(gamma) * np.sin(alpha) * B)

            R_right = (np.cos(gamma) * T + 
                       np.sin(gamma) * np.cos(alpha) * N - 
                       np.sin(gamma) * np.sin(alpha) * B)

            deployed.append((R_left, R_right))
        return deployed
