#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
import ast
import os

import services
from objects import HiddenReasonFlag
from pronouns.modinfo import ModInfo
from pronouns.pronouns import Pronouns
from pronouns.pronouns_store import PronounsStore
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.save_load.common_save_utils import CommonSaveUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.libraries.ts4folders import TS4Folders
from ts4lib.utils.config.pretty_dict import PrettyDict
from ts4lib.utils.singleton import Singleton
from ts4lib.utils.vanilla_names import VanillaNames

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class PronounsManager(metaclass=Singleton):
    FILENAME = 'pronouns'
    INFO = 'Info'
    NAMES = 'names'
    NAME_COLLISIONS = 'name_collision'
    SIM_IDS = 'sim_ids'
    SIMS_DEFAULT_PRONOUNS = 'sims_with_default_pronouns'
    DEFAULT_PRONOUNS = 'default_pronouns'
    DEFAULT = "|||||"

    def __init__(self):
        self.pronouns = Pronouns()
        self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)

    def load(self):
        current_save_slot_guid = CommonSaveUtils().get_save_slot_guid()
        all_pronouns = {}
        for file in f"{PronounsManager.FILENAME}.txt", f"{PronounsManager.FILENAME}.{current_save_slot_guid}.txt":
            filename = os.path.join(self.ts4f.data_folder, file)
            if os.path.exists(filename):
                try:
                    with open(filename, mode='rt', encoding='UTF-8') as fp:
                        data = ast.literal_eval(fp.read())
                        for k, v in data.items():
                            current_v = all_pronouns.get(k, {})
                            for _k, _v in v.items():
                                current_v.update({_k: _v})
                            all_pronouns.update({k: current_v})
                except Exception as e:
                    log.warn(f"Skipping file '{file}' with error '{e}'.")
            else:
                log.debug(f"Skipping '{file}' (file doesn't exit).")
        log.debug(f"loaded pronouns = {all_pronouns}")
        PronounsStore().pronouns = all_pronouns

    def apply(self):
        vn = VanillaNames()
        all_pronouns = PronounsStore().pronouns
        names = all_pronouns.get(PronounsManager.NAMES, None)
        sim_ids = all_pronouns.get(PronounsManager.SIM_IDS, None)

        for sim in CommonSimUtils.get_all_sims_generator():
            sim_id = CommonSimUtils.get_sim_id(sim)
            _, sim_name = vn.get_sim_name(sim_id)
            if names and sim_name in names:
                self.pronouns.set_pronouns(sim, names.get(sim_name))
            elif sim_ids and sim_id in sim_ids:
                self.pronouns.set_pronouns(sim, sim_ids.get(sim_id))

    def clear_all(self):
        vn = VanillaNames()
        for sim in CommonSimUtils.get_all_sims_generator():
            pronouns = self.pronouns.get_pronouns(sim)
            if pronouns == PronounsManager.DEFAULT:
                continue
            sim_id = CommonSimUtils.get_sim_id(sim)
            _, sim_name = vn.get_sim_name(sim_id)
            log.debug(f'CLEAR: {sim_name} ! o19.pronouns {pronouns} {sim_id}')
            self.pronouns.set_pronouns(sim, PronounsManager.DEFAULT)

    def show_all(self):
        vn = VanillaNames()
        for sim in CommonSimUtils.get_all_sims_generator():
            pronouns = self.pronouns.get_pronouns(sim)
            if pronouns == PronounsManager.DEFAULT:
                continue
            sim_id = CommonSimUtils.get_sim_id(sim)
            _, sim_name = vn.get_sim_name(sim_id)
            log.debug(f'SHOW: {sim_name} ! o19.pronouns {pronouns} {sim_id}')

    def save(self):
        """
        Save all pronouns which have been loaded and all pronouns of sims in this game.
        @return:
        """

        all_pronouns = PronounsStore().pronouns
        vn = VanillaNames()
        sims_with_default_pronouns = set()
        duplicate_names = set()
        duplicate_name_sim_ids = set()
        pronouns_data_sim_id = {}
        pronouns_data_name = {}
        sim_id_to_name = {}

        for sim in CommonSimUtils.get_all_sims_generator():
            sim_id = CommonSimUtils.get_sim_id(sim)
            _, sim_name = vn.get_sim_name(sim_id)
            sim_id_to_name.update({sim_id: sim_name})

            pronouns = self.pronouns.get_pronouns(sim)
            pronouns_data_sim_id.update({sim_id: pronouns})

            if sim_name in pronouns_data_name.keys():
                duplicate_names.add(sim_name)
                _sim_id = pronouns_data_name.get(sim_name)
                _sim_id = list(sim_id_to_name.keys())[list(sim_id_to_name.values()).index(sim_name)]

                duplicate_name_sim_ids.add(_sim_id)
                duplicate_name_sim_ids.add(sim_id)

            pronouns_data_name.update({sim_name: pronouns})

        for sim_name in duplicate_names:
            del pronouns_data_name[sim_name]

        for sim_name, pronouns in pronouns_data_name.items():
            if pronouns == PronounsManager.DEFAULT:
                sims_with_default_pronouns.add(sim_name)

        for sim_name in sims_with_default_pronouns:
            del pronouns_data_name[sim_name]

        sim_ids = {}
        for sim_id in duplicate_name_sim_ids:
            sim_ids.update({sim_id: pronouns_data_sim_id.get(sim_id)})

        current_save_slot_guid = CommonSaveUtils().get_save_slot_guid()
        all_pronouns.update({f"{PronounsManager.INFO}.1": f"Rename the file to '{PronounsManager.FILENAME}.txt' to use it as-is for all games."})
        all_pronouns.update({f"{PronounsManager.INFO}.2": f"Rename the file to '{PronounsManager.FILENAME}.{current_save_slot_guid}.txt' to use it as-is for this save game."})
        all_pronouns.update({f"{PronounsManager.INFO}.3": f"It is recommended to keep the config files short and delete all information which is not needed."})
        all_pronouns.update({PronounsManager.NAMES: pronouns_data_name})
        if sims_with_default_pronouns:
            all_pronouns.update({f"{PronounsManager.INFO}.{PronounsManager.SIMS_DEFAULT_PRONOUNS}": sims_with_default_pronouns})
            all_pronouns.update({f"{PronounsManager.INFO}.{PronounsManager.DEFAULT_PRONOUNS}": PronounsManager.DEFAULT})
        if duplicate_name_sim_ids:
            all_pronouns.update({f"{PronounsManager.INFO}.{PronounsManager.NAME_COLLISIONS}": duplicate_name_sim_ids})
        if sim_ids:
            all_pronouns.update({PronounsManager.SIM_IDS: sim_ids})

        filename = os.path.join(self.ts4f.data_folder, f"{PronounsManager.FILENAME}.sample.{current_save_slot_guid}.txt")
        PrettyDict.write(filename, all_pronouns)

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.pronouns.save', 'Save all pronouns.')
    def o19_manage_pronouns_debug_save(output: CommonConsoleCommandOutput):
        PronounsManager().save()
        output(f"Configuration saved.")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.pronouns.load', 'Load all pronouns.')
    def o19_manage_pronouns_debug_load(output: CommonConsoleCommandOutput):
        PronounsManager().load()
        PronounsManager().apply()
        output(f"Configuration loaded.")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.pronouns.clear_all', 'Clear pronouns for all sims.')
    def o19_manage_pronouns_debug_clear_all(output: CommonConsoleCommandOutput):
        PronounsManager().clear_all()
        output(f"Removed all pronouns. See log for details.")


    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.pronouns.show_all', 'Log pronouns of all sims.')
    def o19_manage_pronouns_debug_show_all(output: CommonConsoleCommandOutput):
        PronounsManager().show_all()
        output(f"See log for details.")

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def o19_manage_pronouns_handle_event_start(event_data: S4CLZoneLateLoadEvent):
        PronounsManager().load()