# 🗣️ Pronouns for TS4
This mod allows you to set all pronouns for a Sim at once using a cheat command — no need to open CAS.

You can even set pronouns that aren't available in CAS. However, EA may consider some pronouns offensive.  
There’s no way for this mod to validate or block such entries, so they will be applied regardless.  
**Do not upload Sims with custom pronouns to EA services unless you're sure the words are acceptable.**  
The language itself doesn’t matter — EA checks the content.

## ⚠️ Warning
Vanilla (or modified) pronouns may cause lag in some save games.  
This is a TS4 issue, not caused by this mod.

If you experience lag:
- Try starting a new game.
- Or use `o19.pronouns.clear_all` to remove all pronouns as a workaround.


## 🧑‍💻 Cheat Command
* `o19.pronouns` - Show the current pronouns.
* `o19.pronouns |||||` - Remove custom pronouns.
* `o19.pronouns she|her|her|hers|herself|` - Set pronouns.
* `o19.pronouns she|her|her|hers|herself| 1234` - Set pronouns for a random sim with sim_id 1234.
* `o19.pronouns "she or he|her or his|her|hers|herself|"` - Set pronouns with spaces.
* `o19.pronouns she|"her or his"|her|hers|herself|` - Set pronouns with spaces (alternative).
* `o19.pronouns.show_all` - Show pronouns for all sims. A sim_id can't be specified.
* `o19.pronouns.clear_all` - Remove custom pronouns for all sims. A sim_id can't be specified.


### 📌 Format Rules
- Each pronoun must end with a `|`.
- `|` and `"` cannot be used inside a pronoun.
- Text with more or fewer than 5 `|` will be ignored.
- Anything after the 5th `|` will be discarded.

### 🧠 Pronoun Types and Examples
1. **Subjective**: `She/He/They/______` would like a grilled cheese.  
2. **Objective**: o19 told `her/him/them/______` about the best grilled cheese.  
3. **Possessive Dependent**: Grilled cheese is `her/his/their/______` first love.  
4. **Possessive Independent**: That grilled cheese is `hers/his/theirs/______`.  
5. **Reflexive**: o19 made the grilled cheese `herself/himself/themselves/______`.

## 🔄 Automation
This mod supports saving and loading pronouns for all Sims.  
Custom pronouns are applied automatically when a zone is loaded.

No default file is included, so automation won’t happen until you create one.

### Commands
- `o19.pronouns.save` — Save pronouns to `pronouns.sample.{save_id}.txt`
- `o19.pronouns.load` — Load and apply `pronouns.txt` and `pronouns.{save_id}.txt`

Saved files are informative and won’t overwrite user-created configs.  
To use them for automation:
- Rename the saved file.
- Remove unnecessary entries to keep it short.

### 📁 File Behavior
- `pronouns.txt` — Loaded first. Applies to all games.  
  Use this to assign pronouns to Sims like "Bella Goth" across all saves.  
  Should **not** contain sim_ids.

- `pronouns.{save_id}.txt` — Loaded second. Applies to the current save.  
  Can contain sim_ids unique to that save.

You can also run `o19.pronouns.load` manually for debugging.

### 📝 Sample Files
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

## 🐞 Known Issues
Most pronouns can be viewed and edited in CAS.
If EA flags a pronoun as offensive, changes cannot be saved until it’s removed.
You can either keep the pronouns as-is and cancel editing the sim or clear the offending ones to save the sim.

## 🧭 Alternatives
ControlMenu allows editing names and pronouns via UI. However, it can be time-consuming to set all five pronouns for multiple Sims.

TS4 also supports pronoun editing in CAS — except for entries EA deems inappropriate for unclear reasons.


# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.119.109, S4CL 3.15, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
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

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
