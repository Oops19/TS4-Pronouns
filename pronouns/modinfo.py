from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    """ Mod info for the S4CL Sample Mod. """
    # To create a Mod Identity for this mod, simply do ModInfo.get_identity(). Please refrain from using the ModInfo of The Sims 4 Community Library in your own mod and instead use yours!
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        # This is the name that'll be used whenever a Messages.txt or Exceptions.txt file is created <_name>_Messages.txt and <_name>_Exceptions.txt.
        return 'Pronouns'

    @property
    def _author(self) -> str:
        # This is your name.
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        # This is the name of the root package
        return 'pronouns'

    @property
    def _file_path(self) -> str:
        # This is simply a file path that you do not need to change.
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '2.0.5'


"""
v2.0.5
    Added ability to save and load pronouns for individual sims
        a) for a specific save game id
        b) globally
v2.0.4
    themself >> themselves
v2.0.2
    Updated documentation
v2.0.0
    Fix for TS4 v1.108.+
    Previous version does no longer work due to a code change in TS4.
v1.2.2
    Update README for new TS4 version
v1.2.1
    Updated documentation
v1.2.0
    Regex to remove one '@' within a string. 'B@@Man' > 'B@Man', 'F@@@@hen' > 'F[at][at][At]hen'
v1.0.0
    Initial version
"""
