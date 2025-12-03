# Simple-Minigrid

Simplification of the [Minigrid](https://github.com/Farama-Foundation/Minigrid) library.

Actions are reduced to:  
0 - right  
1 - down  
2 - left  
3 - top  

The agent is drawn as a circle.

## Available Environments
Currently, only the empty Minigrid environments are available.

### Empty
Like in Minigrid.

Environments:  
`SimpleMiniGrid-Empty-5x5-v0`  
`SimpleMiniGrid-Empty-Random-5x5-v0`  
`SimpleMiniGrid-Empty-6x6-v0`  
`SimpleMiniGrid-Empty-Random-6x6-v0`  
`SimpleMiniGrid-Empty-8x8-v0`  
`SimpleMiniGrid-Empty-16x16-v0`  

### Reward
Another `RewardEnv` is added.
`RewardEnv` is an empty environment, while `RewardFourRoomsEnv` is a four rooms environment.
This environment contains reward objects which the agent can collect by walking over them.
Such a reward can only be collected once per episode.
The number of reward objects can be set with `num_objects` and the number of object classes with `num_object_classes`.
Note that the number of objects must be evenly distributable to the classes.
Rewards for each class are uniformly sampled from [-1, 1].

Environments:  
`SimpleMiniGrid-Reward-5x5-v0` - Empty  
`SimpleMiniGrid-Reward-8x8-v0` - Empty  
`SimpleMiniGrid-RewardFourRooms-v0` - FourRooms  

## Getting started
```python
import gymnasium as gym

import simple_minigrid


env = gym.make('SimpleMiniGrid-RewardFourRooms-v0', render_mode='human')

obs, info = env.reset()
while True:
    env.render()
```