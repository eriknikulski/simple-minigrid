from __future__ import annotations

import numpy as np

TILE_PIXELS = 32

CLASSED_REWARD_COLORS = {
    "rc0": np.array([242,  60, 169]),
    "rc1": np.array([242, 169,  60]),
    "rc2": np.array([205, 242,  60]),
    "rc3": np.array([ 96, 242,  60]),
    "rc4": np.array([ 60, 242, 133]),
    "rc5": np.array([ 60, 242, 242]),
    "rc6": np.array([ 60, 133, 242]),
    "rc7": np.array([ 96,  60, 242]),
    "rc8": np.array([205,  60, 242]),
    "rc9": np.array([242,  60,  60]),
}

# Map of color names to RGB values
COLORS = {
    "red": np.array([255, 0, 0]),
    "green": np.array([0, 255, 0]),
    "blue": np.array([0, 0, 255]),
    "purple": np.array([112, 39, 195]),
    "yellow": np.array([255, 255, 0]),
    "grey": np.array([100, 100, 100]),
    **CLASSED_REWARD_COLORS,
}

COLOR_NAMES = sorted(list(COLORS.keys()))

# Used to map colors to integers
COLOR_TO_IDX = {
    "red": 0, "green": 1, "blue": 2, "purple": 3, "yellow": 4, "grey": 5,
    "rc0": 10, "rc1": 11, "rc2": 12, "rc3": 13, "rc4": 14, "rc5": 15, "rc6": 16, "rc7": 17, "rc8": 18, "rc9": 19,
}

IDX_TO_COLOR = dict(zip(COLOR_TO_IDX.values(), COLOR_TO_IDX.keys()))

CLASSED_REWARD_OBJECTS = {
    "reward_object_0": 110,
    "reward_object_1": 111,
    "reward_object_2": 112,
    "reward_object_3": 113,
    "reward_object_4": 114,
    "reward_object_5": 115,
    "reward_object_6": 116,
    "reward_object_7": 117,
    "reward_object_8": 118,
    "reward_object_9": 119,
}

# Map of object type to integers
OBJECT_TO_IDX = {
    "unseen": 0,
    "empty": 1,
    "wall": 2,
    "floor": 3,
    "door": 4,
    "key": 5,
    "ball": 6,
    "box": 7,
    "goal": 8,
    "lava": 9,
    "agent": 10,
    **CLASSED_REWARD_OBJECTS,
}

IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(), OBJECT_TO_IDX.keys()))

# Map of state names to integers
STATE_TO_IDX = {
    "open": 0,
    "closed": 1,
    "locked": 2,
}

# Map of direction indices to vectors
DIR_TO_VEC = [
    # Pointing right (positive X)
    np.array((1, 0)),
    # Down (positive Y)
    np.array((0, 1)),
    # Pointing left (negative X)
    np.array((-1, 0)),
    # Up (negative Y)
    np.array((0, -1)),
]
