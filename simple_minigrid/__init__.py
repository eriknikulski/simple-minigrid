from __future__ import annotations

from gymnasium.envs.registration import register

from simple_minigrid import simple_minigrid_env, wrappers
from simple_minigrid.core import roomgrid
from simple_minigrid.core.world_object import Wall

__version__ = "2.5.0"


def register_minigrid_envs():
    # Empty
    # ----------------------------------------

    register(
        id="SimpleMiniGrid-Empty-5x5-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
        kwargs={"size": 5},
    )

    register(
        id="SimpleMiniGrid-Empty-Random-5x5-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
        kwargs={"size": 5, "agent_start_pos": None},
    )

    register(
        id="SimpleMiniGrid-Empty-6x6-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
        kwargs={"size": 6},
    )

    register(
        id="SimpleMiniGrid-Empty-Random-6x6-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
        kwargs={"size": 6, "agent_start_pos": None},
    )

    register(
        id="SimpleMiniGrid-Empty-8x8-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
    )

    register(
        id="SimpleMiniGrid-Empty-16x16-v0",
        entry_point="simple_minigrid.envs:EmptyEnv",
        kwargs={"size": 16},
    )

    # Reward
    # ----------------------------------------

    register(
        id="SimpleMiniGrid-Reward-5x5-v0",
        entry_point="simple_minigrid.envs:RewardEnv",
        kwargs={"size": 5, "num_objects": 2, "num_object_classes": 2},
    )

    register(
        id="SimpleMiniGrid-Reward-8x8-v0",
        entry_point="simple_minigrid.envs:RewardEnv",
        kwargs={"size": 8, "num_objects": 4, "num_object_classes": 2},
    )


register_minigrid_envs()

try:
    import sys

    from farama_notifications import notifications

    if "minigrid" in notifications and __version__ in notifications["minigrid"]:
        print(notifications["minigrid"][__version__], file=sys.stderr)
except Exception:  # nosec
    pass
