#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict

from ts4lib.utils.singleton import Singleton


class PronounsStore(metaclass=Singleton):

    def __init__(self):
        self._pronouns = {}

    @property
    def pronouns(self) -> Dict:
        return self._pronouns

    @pronouns.setter
    def pronouns(self, pronouns: Dict):
        self._pronouns = pronouns