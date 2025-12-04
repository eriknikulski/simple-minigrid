from typing import Optional

import numpy as np

from simple_minigrid.core.grid import Grid
from simple_minigrid.core.mission import MissionSpace
from simple_minigrid.core.world_object import RewardObject, Goal
from simple_minigrid.envs.utils import get_surrounding_wall_positions
from simple_minigrid.simple_minigrid_env import SimpleMiniGridEnv


def get_random_positions(
        width: int,
        height: int,
        n_positions: int,
        n_classes: int,
        avoid: Optional[np.ndarray] = None,
        rng: Optional[np.random.Generator] = None,
) -> np.ndarray:
    """
    Sample `n_positions` unique positions in a width x height grid, optionally avoiding some positions,
    and partition into `n_classes` groups.

    Parameters:
        width : int
        height : int
        n_positions : int
        n_classes : int
        avoid : np.ndarray of shape (M, 2), positions to avoid
        rng: np.random.Generator
    Returns:
        np.ndarray of shape (n_classes, n_positions_per_class, 2)
    """
    assert n_positions % n_classes == 0

    if rng is None:
        rng = np.random.default_rng()

    total_positions = width * height

    if avoid is not None and len(avoid) > 0:
        # Convert (x, y) positions to linear indices
        avoid_idx = avoid[:, 0] * width + avoid[:, 1]
        # All available indices
        available_idx = np.setdiff1d(np.arange(total_positions), avoid_idx)
    else:
        available_idx = np.arange(total_positions)

    if n_positions > len(available_idx):
        raise ValueError('Not enough available positions to sample from.')

    # Sample N unique linear indices
    idx = rng.choice(available_idx, n_positions, replace=False)
    positions = np.column_stack((idx // width, idx % width))
    # Partition into K groups
    return positions.reshape(n_classes, -1, 2)


class RewardEnv(SimpleMiniGridEnv):
    def __init__(
        self,
        size=8,
        agent_start_pos=(1, 1),
        max_steps: int | None = None,
        num_objects: int | None = None,
        num_object_classes: int | None = None,
        **kwargs,
    ):
        assert ((num_objects is None or 0 <= num_objects) and
                (num_object_classes is None or num_objects % num_object_classes == 0))
        assert num_object_classes is None or 0 <= num_object_classes <= 10

        self.agent_start_pos = agent_start_pos
        self.num_objects = num_objects
        self.num_object_classes = num_object_classes if num_object_classes is not None else num_objects
        self.rewards = self.np_random.uniform(low=-1, high=1, size=self.num_object_classes)

        mission_space = MissionSpace(mission_func=self._gen_mission)

        if max_steps is None:
            max_steps = 4 * size**2

        super().__init__(
            mission_space=mission_space,
            grid_size=size,
            # Set this to True for maximum speed
            see_through_walls=True,
            max_steps=max_steps,
            **kwargs,
        )

    @staticmethod
    def _gen_mission():
        return "get to the green goal square"

    def place_reward_objs(
            self,
            width: int,
            height: int,
            avoid: Optional[np.ndarray] = None,
            remove_walls: bool = True,
    ) -> None:
        obj_per_class = self.num_objects // self.num_object_classes

        if remove_walls:
            walls = get_surrounding_wall_positions(width, height)
            if avoid is None:
                avoid = walls
            else:
                avoid = np.concatenate([avoid, walls])

        # shift to ignore border
        positions = get_random_positions(
            width=width,
            height=height,
            n_positions=self.num_objects,
            n_classes=self.num_object_classes,
            avoid=avoid,
            rng=self.np_random,
        )

        for obj_class in range(self.num_object_classes):
            for i in range(obj_per_class):
                x_pos, y_pos = positions[obj_class, i].tolist()
                reward = self.rewards[obj_class].item()

                self.put_obj(RewardObject(obj_class, reward), x_pos, y_pos)

    def _gen_grid(self, width: int, height: int) -> None:
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal square in the bottom-right corner
        goal_pos = (width - 2, height - 2)
        self.put_obj(Goal(), *goal_pos)

        # Place the agent
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
        else:
            self.place_agent()

        # Place reward objects
        self.place_reward_objs(width, height, avoid=np.array([[*self.agent_pos], [*goal_pos]]))

        self.mission = "get to the green goal square"
