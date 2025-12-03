import numpy as np


def get_surrounding_wall_positions(width: int, height: int) -> np.ndarray:
    # Create grid coordinates
    x = np.arange(width)
    y = np.arange(height)

    # Top and bottom rows
    top_bottom = np.array([(xi, 0) for xi in x] + [(xi, height - 1) for xi in x])

    # Left and right columns (excluding corners)
    left_right = np.array([(0, yi) for yi in y[1:-1]] + [(width - 1, yi) for yi in y[1:-1]])

    # Combine all
    walls = np.vstack([top_bottom, left_right])
    return walls
