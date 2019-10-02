import random
import numpy as np

from rlcard.envs.env import Env
from rlcard.games.uno.game import UnoGame as Game
from rlcard.games.uno.utils import encode_hand, encode_target
from rlcard.games.uno.utils import ACTION_SPACE, ACTION_LIST


class UnoEnv(Env):

    def __init__(self, allow_step_back=False):
        super().__init__(Game(allow_step_back), allow_step_back)
        self.state_shape = [7, 4, 15]

    def extract_state(self, state):
        obs = np.zeros((7, 4, 15), dtype=int)
        encode_hand(obs[:3], state['hand'])
        encode_target(obs[3], state['target'])
        encode_hand(obs[4:], state['others_hand'])
        legal_action_id = self.get_legal_actions()
        extrated_state = {'obs': obs, 'legal_actions': legal_action_id}
        return extrated_state

    def get_payoffs(self):

        return self.game.get_payoffs()

    def decode_action(self, action_id):
        legal_ids = self.get_legal_actions()
        if action_id in legal_ids:
            return ACTION_LIST[action_id]
        #if (len(self.game.dealer.deck) + len(self.game.round.played_cards)) > 17: 
        #    return ACTION_LIST[60]
        return ACTION_LIST[np.random.choice(legal_ids)]

    def get_legal_actions(self):
        legal_actions = self.game.get_legal_actions()
        legal_ids = [ACTION_SPACE[action] for action in legal_actions]
        return legal_ids
