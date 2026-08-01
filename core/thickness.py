import numpy as np

class Strip:
    def __init__(self, analyzer, rulings, width=0.1, thickness=0.008, axis_shift='center'):
        self.analyzer = analyzer
        self.centerline = np.array(analyzer.points)
        self.rulings = rulings
        self.width = width
        self.thickness = thickness
        self.axis_shift = axis_shift

        self.left_edge = []
        self.right_edge = []
        self.offset_left = []
        self.offset_right = []

        self._compute_edges()
        self._apply_thickness()

    def _compute_edges(self):
        for pt, (R_left, R_right) in zip(self.centerline, self.rulings):
            left = pt + self.width * R_left
            right = pt + self.width * R_right
            self.left_edge.append(left)
            self.right_edge.append(right)

    def _apply_thickness(self):
        # simple axis shift approximation: shift along (ruling x tangent)
        for i, pt in enumerate(self.centerline):
            R_left, _ = self.rulings[i]
            T = self.analyzer.tangents[i]
            n = np.cross(R_left, T)
            n_norm = np.linalg.norm(n)
            if n_norm < 1e-12:
                n = np.array([0.0, 0.0, 1.0])
            else:
                n = n / n_norm
            offset = (self.thickness / 2.0) * n
            self.offset_left.append(self.left_edge[i] + offset)
            self.offset_right.append(self.right_edge[i] + offset)
