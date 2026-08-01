import numpy as np

class CurveAnalyzer:
    """Discrete curve analyser: samples a parametric curve and computes Frenet frames."""

    def __init__(self, curve_callable, resolution=50):
        self.curve = curve_callable
        self.resolution = resolution
        self.points = []
        self.tangents = []
        self.normals = []
        self.binormals = []
        self.curvatures = []
        self._discretize_and_analyze()

    def _discretize_and_analyze(self):
        dt = 1.0 / (self.resolution - 1)
        for i in range(self.resolution):
            t = i * dt
            pt = np.asarray(self.curve.eval_point(t))
            d1 = np.asarray(self.curve.eval_derivative(t, 1))
            d2 = np.asarray(self.curve.eval_derivative(t, 2))

            self.points.append(pt)

            v = d1
            norm_v = np.linalg.norm(v)
            if norm_v < 1e-12:
                T = np.array([1.0, 0.0, 0.0])
            else:
                T = v / norm_v

            # curvature
            cross = np.cross(d1, d2)
            kappa = np.linalg.norm(cross) / (norm_v ** 3) if norm_v > 1e-12 else 0.0

            if kappa > 1e-8:
                # normal component
                n = d2 - np.dot(d2, T) * T
                n_norm = np.linalg.norm(n)
                if n_norm < 1e-12:
                    N = self._perpendicular_to(T)
                else:
                    N = n / n_norm
            else:
                N = self._perpendicular_to(T)

            B = np.cross(T, N)
            B = B / np.linalg.norm(B)

            self.tangents.append(T)
            self.normals.append(N)
            self.binormals.append(B)
            self.curvatures.append(kappa)

    @staticmethod
    def _perpendicular_to(v):
        v = np.asarray(v)
        if abs(v[2]) < 0.9:
            perp = np.cross([0, 0, 1], v)
        else:
            perp = np.cross([1, 0, 0], v)
        n = np.linalg.norm(perp)
        if n < 1e-12:
            return np.array([0.0, 1.0, 0.0])
        return perp / n
