import numpy as np
from .rulings import RulingCalculator
from .multi_crease import MultiCreaseVault

class Deployment:
    def __init__(self, vault, analyzer):
        self.vault = vault
        self.analyzer = analyzer

    def deploy(self, alpha_target):
        deployed_rulings_list = []
        for strip in self.vault.strips:
            ruling_calc = RulingCalculator(self.analyzer)
            deployed = ruling_calc.get_ruling_at_deployment(alpha_target)
            deployed_rulings_list.append(deployed)

        # reconstruct strips naively
        deployed_vault = MultiCreaseVault(self.vault.base_strip, self.vault.num_strips, self.vault.plane_distance)
        # TODO: proper reconstruction using Eq. (8)
        return deployed_vault
