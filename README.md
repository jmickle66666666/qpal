# qpalconvert.py
Convert between quake palette files and png

Requires python 3, and PIL imaging library

Usage:

`python qpalconvert.py palette.lmp`

Converts a palette file from quake (found in `id1/PAK0.pak/gfx`) to a PNG image representation of the palette


`python qpalconvert.py palette.png`

Converts a 16x16 image file into a quake palette lump.


To use the new palette in your mod, place it in your mod folder at `your_mod/gfx/palette.lmp`
