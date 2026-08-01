import pytest
import numpy as np
from examples.simple_arc import ArcCurve
from core.curve_analysis import CurveAnalyzer

def test_frenet_basic():
    curve = ArcCurve(radius=1.0, height=0.0)
    analyzer = CurveAnalyzer(curve, resolution=16)
    assert len(analyzer.points) == 16
    assert len(analyzer.tangents) == 16
    assert len(analyzer.normals) == 16
