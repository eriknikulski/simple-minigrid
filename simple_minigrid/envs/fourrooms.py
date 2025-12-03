from typing import Tuple

import numpy as np

from simple_minigrid.core.grid import Grid
from simple_minigrid.core.world_object import Goal
from simple_minigrid.envs import RewardEnv


class RewardFourRoomsEnv(RewardEnv):
    def __init__(
            self,
            agent_pos: Tuple[int, int] = None,
            goal_pos: Tuple[int, int] = None,
            max_steps: int = 100,
            **kwargs,
    ) -> None:
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos

        size = 19

        super().__init__(
            size=size,
            max_steps=max_steps,
            **kwargs,
        )

    def _gen_grid(self, width: int, height: int) -> None:
        """
        Mainly copied from minigrids FourRoomsEnv

        :param width:
        :param height:
        :return: None
        """
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        room_w = width // 2
        room_h = height // 2

        wall_positions = []
        # For each row of rooms
        for j in range(0, 2):
            # For each column
            for i in range(0, 2):
                xL = i * room_w
                yT = j * room_h
                xR = xL + room_w
                yB = yT + room_h

                # Bottom wall and door
                if i + 1 < 2:
                    self.grid.vert_wall(xR, yT, room_h)
                    pos = (xR, self._rand_int(yT + 1, yB))
                    self.grid.set(*pos, None)
                    wall_positions.extend([(xR, yT + i) for i in range(room_h) if (xR, yT + i) != pos])

                # Bottom wall and door
                if j + 1 < 2:
                    self.grid.horz_wall(xL, yB, room_w)
                    pos = (self._rand_int(xL + 1, xR), yB)
                    self.grid.set(*pos, None)
                    wall_positions.extend([(xL + i, yB) for i in range(room_w) if (xR, yT + i) != pos])

        # Randomize the player start position and orientation
        if self._agent_default_pos is not None:
            self.agent_pos = self._agent_default_pos
            self.grid.set(*self._agent_default_pos, None)
            # assuming random start direction
            self.agent_dir = self._rand_int(0, 4)
        else:
            self.place_agent()

        if self._goal_default_pos is not None:
            goal = Goal()
            self.put_obj(goal, *self._goal_default_pos)
            goal.init_pos, goal.cur_pos = self._goal_default_pos
            goal_pos = self._goal_default_pos
        else:
            goal_pos = self.place_obj(Goal())

        # Place reward objects
        self.place_reward_objs(
            width=width,
            height=height,
            avoid=np.array([
                [*self.agent_pos],
                [*goal_pos],
                *[[*pos] for pos in wall_positions],
            ]),
        )