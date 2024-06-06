#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


import re

from pronouns.modinfo import ModInfo

from sims.sim_info_base_wrapper import SimInfoBaseWrapper

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()
log.debug(f"Starting {ModInfo.get_identity().name} v{ModInfo.get_identity().version}")


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfoBaseWrapper, 'packed_pronouns', handle_exceptions=False)
def o19_injected_packed_pronouns(original, self):
    rv = original(self)
    try:
        rv = re.sub(f"([a-zA-Z])@(@*[a-zA-Z])", r"\g<1>\g<2>", rv)
    except Exception as e:
        log.error(f"re() error '{e}'.", throw=False)
    return rv


log.debug(f"Injected into packed_pronouns")
