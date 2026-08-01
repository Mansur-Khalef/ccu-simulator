import numpy as np
from .thickness import Strip

class MultiCreaseVault:
    def __init__(self, base_strip, num_strips=3, plane_distance=0.12, inclination_mode='parallel'):
        self.base_strip = base_strip
        self.num_strips = num_strips
        self.plane_distance = plane_distance
        self.inclination_mode = inclination_mode
        self.strips = [base_strip]
        self._generate_additional_strips()

    def _generate_additional_strips(self):
        for i in range(1, self.num_strips):
            offset_dir = self._get_offset_direction(i)
            offset_amount = i * self.plane_distance
            new_centerline = [pt + offset_amount * offset_dir for pt in self.base_strip.centerline]
            new_strip = Strip(self.base_strip.analyzer, self.base_strip.rulings, self.base_strip.width, self.base_strip.thickness)
            new_strip.centerline = new_centerline
            self.strips.append(new_strip)

    def _get_offset_direction(self, i):
        return self.base_strip.analyzer.binormals[0]
