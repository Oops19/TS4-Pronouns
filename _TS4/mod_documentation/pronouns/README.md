#  Pronouns for TS4
This mod allows to set all pronouns for a sim at once with a cheat command without using CAS.

Setting pronouns which can't be set in CAS is possible and EA might consider these as offending.
There is unfortunately no way to check and block offending pronouns from within this mod, so they will be set no matter what they are.
Do not upload a sim with pronouns set with ths mood to any EA service unless you are sure that the words are not considered by EA to be offending - the language itself doesn't really matter.

#### Warning
Vanilla (or modified) pronouns may cause some lag for some save games.
This is not caused by this mod, it's a TS4 feature.
If this is the case starting a completely new game may fix the issue.
Otherwise, remove all pronouns (with `o19.pronouns.clear_all`) as a workaround. 

## Cheat Command
* `o19.pronouns` - Show the current pronouns.
* `o19.pronouns |||||` - Remove custom pronouns.
* `o19.pronouns she|her|her|hers|herself|` - Set pronouns.
* `o19.pronouns she|her|her|hers|herself| 1234` - Set pronouns for a random sim with sim_id 1234.
* `o19.pronouns "she or he|her or his|her|hers|herself|"` - Set pronouns with spaces.
* `o19.pronouns she|"her or his"|her|hers|herself|` - Set pronouns with spaces (alternative).
* `o19.pronouns.show_all` - Show pronouns for all sims. A sim_id can't be specified.
* `o19.pronouns.clear_all` - Remove custom pronouns for all sims. A sim_id can't be specified.
* 
Each pronoun must end with a '|'.
The '|' and/or '"' characters can't be used in a pronoun.
Pronoun texts with more or less than 5 '|' will be ignored.
Text after the 5th '|' will be discarded.

#### Type and order of pronouns with examples:
1. Subjective: `She/He/They/______` would like a grilled cheese.
2. Objective: o19 told `her/him/them/______` about the best grilled cheese.
3. Possessive Dependent: Grilled cheese is `her/his/their/______` 1st love.
4. Possessive Independent: That grilled cheese is `hers/his/theirs/______`.
5. Reflexive: o19 made the grilled cheese `herself/himself/themselves/______`.

## Automation
This version also allows to save and load pronouns for all sims.
Custom pronouns will be loaded and applied whenever a zone is loaded.
No default file is included so no automation will happen after installing this mod.

### Commands
* `o19.pronouns.save` - Save the pronouns to `pronouns.sample.{save_id}.txt`
* `o19.pronouns.load` - Load and apply `pronouns.txt` and `pronouns.{save_id}.txt`

Saving pronouns does not automatically add them to a file which will be read.
Saving will create files with informative data and never modify a user-created configuration file.
The saved file needs to be renamed and one should remove all pronouns which are not needed to keep the file short.

The file `pronouns.txt` will be loaded first and can be used to set pronouns for all games.
To assign new pronouns to all 'Bella Goth' sims in all games this is the right file.
It should not contain any sim_id .

The file `pronouns.{save_id}.txt` will be loaded afterwards.
To assign new pronouns to all 'Bella Goth' sims in this save game use this file.
It may also contain sim_id's which are unique in each save game.

The `o19.pronouns.load` can be used to load the files for debugging purposes.

#### Samples files:
`pronouns.txt`
```json
{
  "names":{
    "Cindy#Rella": "he|him|his|his|himself|",
  }, 
}
```
`pronouns.123.txt`
```json
{
  "names": {
    "Cindy#Rella": "he|him|his|his|himself|"
  },
}
```
In each played and new game Cindy will be 'he'.
Except of the save with ID 123 - there Cindy will be 'them'.

The save game ID is written with `o19.pronouns.save` to the file name.

### Known Issues
Most set pronouns can be viewed and edited in CAS.
In case EA accidentally considers one of the pronouns as offending changes to the pronouns can not be saved before removing the offending pronoun(s).
Either keep the pronouns as-is or clear offending words.

### Alternatives
ControlMenu has the option to modify the name and pronouns of sims.
It's in the menu and can be a little bit time consuming to set all 5 pronouns for multiple sims.

Setting the pronouns in TS4 is also possible, except for pronouns which are considered inappropriate by EA for random reasons.


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.112.519, S4CL 3.10, TS4Lib 0.3.36.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Removal of the mod
The mod installation with unzip writes to a few directories.
To remove this mod and all related files locate the files and folders and remove them:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods locate these folders and remove them:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
 
## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*` and/or `mod_sources/$mod_name/*`
* CAS and build-buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.
* `mod_documentation/$mod_name/` and/or `mod_sources/$mod_name/` are not required and can be deleted.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this.
You can extract the ZIP file to a temporary directory and copy the folders manually.
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The files in `ZIP-File/mod_sources` are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Troubleshooting
When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
