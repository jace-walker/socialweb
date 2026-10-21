# this test was given to me by claude and will go through and make my own later..

from agent import Agent
from config import CHEAT


def test_betrayal_lowers_maya_trust():
    # Set up: section 6's Maya and Leo, with Maya trusting Leo at 0.70
    maya = Agent(0, "Maya", {"extraversion": 0.8, "agreeableness": 0.6,
                             "neuroticism": 0.7, "honesty": 0.8})
    leo = Agent(1, "Leo", {"extraversion": 0.5, "agreeableness": 0.7,
                           "neuroticism": 0.3, "honesty": 0.9})
    maya.set_trust(leo.agent_id, 0.70)

    # Act: Leo cheats, so Maya reacts to it
    maya.trust_update(leo.agent_id, CHEAT)

    # Check: 0.70 - (0.15 + 0.35 * 0.7) = 0.305
    assert abs(maya.get_trust(leo.agent_id) - 0.305) < 0.01

