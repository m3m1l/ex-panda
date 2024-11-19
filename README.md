## Configuration

Ex-panda now has a very limited GUI.
Abbreviations can be added in the main window. Just add the abrreviation name in the left input entry, target in the right and press "add new".
If abbreviation already exists, but the target is different, the target will be updated upon pressing the "add new" button.
As of now the window can't be scrollable so if you have many abbreviations they won't show up. 
Also, abbreviations can't be removed (yet), if you want to remove one you need to do it manually by from the "abbreviations.json" file (make sure it's formatted properly).

**It's highly recommended to add a special character like _ at the beginning of your abbreviations to avoid accidental text expansions.**

If you want to use your own trigger to expand your text instead of hitting space, edit the config.ini file:

    trigger=space                   # Default value = space. Can be a letter or a special character (e.g. esc)
    match_suffix=True               # Set to false if you don't want suffix matches (check LIMITATIONS for more info)

## Migrating from earlier versions

If you used ex-panda version 0.3 or lower, you'll need to migrate your abbreviations file using the script located in the "misc" folder.
Just put your "abbrv_list.txt" file in the misc folder, run the script (json_migrator.py) and replace the created "abbreviations.json" file in the main folder.

## LIMITATIONS

The program utilizes [the python keyboard module](https://pypi.org/project/keyboard/), which reads user's keyboard input char by char.
This allows for easy system-wide funcionality, but all of the limitations that affect the original keyboard module affect this program too.
For example, in order to run this program on Linux root is needed to read device files /dev/input/input*

---

Sometimes it's necessary to re-write the whole key, as the chain of inputs won't be recognized as valid sequence of characters anymore.
Also, if we input a character that is not a part of the key before, it won't be replaced. 
The last input before the key must be a non-alphanumeric/special character.
This behaviour is intended to avoid situations where the suffix of one word is the key of another word. 
For example, if we have a key called 'pet', the word carpet will be expanded to car**expanded text**

This can be disabled by setting the match_suffix value in config.ini to True.
This is helpful when using personal shortcut and not the default trigger (space)

### Other limitations

- Polish and other similar language-specific characters are not supported, only `ASCII`
- Shortcuts can't be used as triggers as they invoke OS-specific behaviour. It's recommended to use the default space or a singular character (e.g. `)