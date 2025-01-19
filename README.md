## Configuration
Make sure Python 3.x is installed on your device before running this app.
Abbreviations can be added and removed in the main app window using the "Add New" button. White characters (space, tab) are not allowed in the abbreviation field for obvious reasons.

To add one, add the abbreviation name in the top entry, target in the bottom and press confimation (thumbs up) button.
To remove an abbreviation, press the X button next to it in the main app window and confirm.
To rename an existing abbreviation, press the edit (pencil) icon next to it and replace the current value with a new one.
When creating/renaming abbreviations, it's okay to use newline characters (enter). Additionally all unicode characters are supported.
If there are too many abbreviations to fit within a window, they can be scrolled.

**It's highly recommended to add a special character like _ at the beginning of your abbreviations to avoid accidental text expansions.**

## Usage
To expand abbreviation to it's target, simply write it using your keyboard and press "space".
If you make a mistake while writing, you need to rewrite the whole abbreviation, using backspace to correct it unfortunately won't work.
The app will register inputs for up to 5 seconds, you must hit space within those 5 seconds, otherwise the text will not be expanded.
Application has a global scope, meaning it will register inputs and expand text inside any program in the system.
Be careful with abbreviations that include newline characters as some programs treat them in a special way! (usually the result is the same as pressing the "enter" key)

If the app becomes dysfunctional (abbreviations are not working/displayed) press the "refresh" button located in the top left corner to reload the app.

## LIMITATIONS

The program utilizes [the python keyboard module](https://pypi.org/project/keyboard/), which reads user's keyboard input char by char.
This allows for easy system-wide funcionality, but all of the limitations that affect the original keyboard module affect this program too.

---
To make app more comfortable to use, the match suffix option is on by default. This means if one abbreviation is a suffix to some word, there may be an accidental text expansion.
For example, if we have an abbreviation named "pet" and we input word car**pet**, the **pet** part will be expanded to the configured target.
To avoid this, I highly recommend to put a special character at the beginning of all abrreviations (e.g. !pet _pet ?pet etc.)

Sometimes it's necessary to re-write the whole key, as the chain of inputs won't be recognized as valid sequence of characters anymore.
This is a standard behaviour of the python keyboard module that was not modified.


### Other limitations

- Only space can be used as the expand button.
- Linux is not supported, app was only tested and verified to work on Windows.
