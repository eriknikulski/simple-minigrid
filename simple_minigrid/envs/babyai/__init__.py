from __future__ import annotations

from simple_minigrid.envs.babyai.goto import (
    GoTo,
    GoToDoor,
    GoToImpUnlock,
    GoToLocal,
    GoToObj,
    GoToObjDoor,
    GoToRedBall,
    GoToRedBallGrey,
    GoToRedBallNoDists,
    GoToRedBlueBall,
    GoToSeq,
)
from simple_minigrid.envs.babyai.open import (
    Open,
    OpenDoor,
    OpenDoorsOrder,
    OpenRedDoor,
    OpenTwoDoors,
)
from simple_minigrid.envs.babyai.other import (
    ActionObjDoor,
    FindObjS5,
    KeyCorridor,
    MoveTwoAcross,
    OneRoomS8,
)
from simple_minigrid.envs.babyai.pickup import (
    Pickup,
    PickupAbove,
    PickupDist,
    PickupLoc,
    UnblockPickup,
)
from simple_minigrid.envs.babyai.putnext import PutNext, PutNextLocal
from simple_minigrid.envs.babyai.synth import (
    BossLevel,
    BossLevelNoUnlock,
    MiniBossLevel,
    Synth,
    SynthLoc,
    SynthSeq,
)
from simple_minigrid.envs.babyai.unlock import (
    BlockedUnlockPickup,
    KeyInBox,
    Unlock,
    UnlockLocal,
    UnlockPickup,
    UnlockToUnlock,
)
