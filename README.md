## Configuration

File called abbrv_list.txt should be formatted in the following way (key and values in one line, in apostrophes, seperated by space):

    'txt' 'text that will appear in place of txt'

If we want to add a newline, the \n character should be used:

    'txt' 'blah blah blah\nnew line\nblah blah blah'

Result:
    
    bla bla bla
    new line
    bla bla bla


IMPORTANT!! If we want to use apostrophes in the expandable text part, it must be escaped with \

For example:
   
    '_hi' 'Hello, it\'s your favourite boy, m3m1l'

Which gives us:

    Hello, it's your favourite boy, m3m1l

Don't use apostrophes in the first part, as it will confuse the program.

    'a'b' 'text to appear' <--- Wrong

If you want to use your own shortcut to expand your text instead of hitting space, edit the config.ini file:

    use_shortcut=True           # Must be set to true
    shrtct=alt+`                #


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
- Some shortcuts cannot be used as they may be utilized by other parts of the system or a program