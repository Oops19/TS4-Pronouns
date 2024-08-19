#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Union

from pronouns.modinfo import ModInfo
from sims.sim import Sim
from sims.sim_info import SimInfo

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()
log.debug(f"Starting {ModInfo.get_identity().name} v{ModInfo.get_identity().version}")


class Pronouns:
    @staticmethod
    def set_pronouns(sim: Sim, pronouns: str = None) -> bool:
        _sim_info = getattr(sim, '_sim_info')
        if _sim_info:
            _base = getattr(_sim_info, '_base')
            if _base:
                packed_pronouns = _base.packed_pronouns
                if pronouns and pronouns != packed_pronouns:
                    _base.packed_pronouns = pronouns
                    log.info(f"'{sim}'s pronouns changed from '{packed_pronouns}' to '{pronouns}'")
                    return True
                else:
                    log.debug(f"'{sim}'s pronouns: '{packed_pronouns}' (not modified).")
            else:
                log.warn(f"Could not get 'SimInfoBaseWrapper' for '{sim}'.")
        else:
            log.warn(f"Could not get 'SimInfo' for '{sim}'.")
        return False

    @staticmethod
    def get_pronouns(sim: Sim) -> Union[str, None]:
        _sim_info = getattr(sim, '_sim_info')
        if _sim_info:
            _base = getattr(_sim_info, '_base')
            if _base:
                return _base.packed_pronouns
            else:
                log.warn(f"Could not get 'SimInfoBaseWrapper' for '{sim}'.")
        else:
            log.warn(f"Could not get 'SimInfo' for '{sim}'.")
        return None

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.pronouns', 'Manage pronouns.',
                          command_arguments=(
                                  CommonConsoleCommandArgument('pronouns', 'Text', "Five pronouns, each ending with '|'", is_optional=True, default_value=''),
                                  CommonConsoleCommandArgument('sim_info', 'Sim Id', 'The decimal identifier of the Sim to use.', is_optional=True, default_value='Active Sim'),
                          )
                          )
    def o19_debug_manage_pronouns(output: CommonConsoleCommandOutput, pronouns: str = None, sim_info: SimInfo = None):
        sim = None
        output(f"{sim_info}")
        if pronouns:
            if len(pronouns.split('|')) != 6:
                output(f"Can't use supplied pronouns! Use '|||||' to remove them or try 'she|her|her|hers|herself|',  'he|him|his|his|himself|' or 'they|them|their|theirs|themselves|'.")
                pronouns = None
            if sim_info:
                sim = CommonSimUtils.get_sim_instance(sim_info)
        if sim is None:
            sim = CommonSimUtils.get_active_sim()
        rv = Pronouns.set_pronouns(sim, pronouns=pronouns)
        if rv is True:
            output(f"Pronouns for '{sim}' are now '{pronouns}'")
        else:
            output(f"Pronouns for '{sim}' not modified.")
