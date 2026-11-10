import numpy as np


def sonar_to_pointcloud(ranges, angles, max_range=8.0):
    points = []
    for r, a in zip(ranges, angles):
        if 0.3 < r < max_range:
            points.append((r * np.cos(a), r * np.sin(a), r))
    return np.asarray(points, dtype=np.float32)
