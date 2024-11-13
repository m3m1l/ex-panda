## Configuration

Ex-panda useds json config file called abbreviations.json. As of now abbreviations and targets must be added manually, following the example config's schema.
This will be changed once GUI is introduced.

If you want to use your own trigger to expand your text instead of hitting space, edit the config.ini file:

    trigger=space                   # Default value = space. Can be a letter or a special character (e.g. esc)
    match_suffix=True               # Set to false if you don't want suffix matches (check LIMITATIONS for more info)


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