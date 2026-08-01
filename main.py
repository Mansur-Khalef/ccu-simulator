import core
from examples.simple_arc import ArcCurve

def demo():
    curve = ArcCurve(radius=1.0, height=0.0)
    analyzer = core.CurveAnalyzer(curve, resolution=64)
    rulings = core.RulingCalculator(analyzer)
    strip = core.Strip(analyzer, rulings.ruling_vectors, width=0.1, thickness=0.01)
    vault = core.MultiCreaseVault(strip, num_strips=5, plane_distance=0.12)
    deployer = core.Deployment(vault, analyzer)
    deployed = deployer.deploy(np.pi/4)
    print("Demo complete. Generated", len(vault.strips), "strips")

if __name__ == '__main__':
    demo()
