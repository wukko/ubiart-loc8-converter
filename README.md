# ubiart-loc8-converter
UbiArt localisation file converter that can be used for modding Just Dance, Rayman Legends, and other UbiArt games.
This Python script lets you decompress, compress, and patch loc8 files easily.

## Why?
`.loc8` files are used for localisation in UbiArt Framework games. This script lets you easily extract or modify those files. It has been used personally by me for many years to create mods for Just Dance.

## Supported games
- Just Dance 2015 - 2022 on all platforms (probably Just Dance 2014 too, haven't tested it)
- Rayman Legends
- Rayman Origins
- ...most likely any other UbiArt game in existence

## How to use it
This script doesn't depend on any external modules. All you need is Python 3+.

However, this script requires passing parameters when used standalone:

```
py loc8Converter.py <mode> <input> <output>

Modes:
-d --decompress     Decompresses the loc8 file as JSON
-c --compress       Compresses the file back to loc8 from JSON
-p --patch          Patches the output JSON file with values in input JSON file

Sample usage:
py loc8Converter.py -d localisation.loc8 localisation.json
```


Step-by-step usage tutorial:
1. Download `loc8Converter.py`
2. Copy it to any desired work directory
3. Run it by opening command prompt or terminal in directory and running `py loc8Converter.py` with parameters listed above

You can also use this script as a module (like I usually do).
