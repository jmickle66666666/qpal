# qpalconvert.py
Convert between quake palette files and png, to create new cool palettes for quake

![preview](https://github.com/jmickle66666666/qpal/blob/master/preview.png)

### Usage

#### windows/mac

Open up `palette.png` in your favourite image editor, and modify it however you'd like. Change the constrast/saturation etc for cool effects and then save it. (You can save it as any file)

In the commandline you can type `qpalconvert my_new_palette.png` and it will output `palette.lmp`, which can be used in your quake mod. Place it in the folder `my_quake_mod/gfx/` folder.

On windows, you can also just drag and drop your image onto `qpalconvert.exe` and it will work without having to use the commandline.

#### python

Requires python 3, and PIL imaging library

`python qpalconvert.py palette.lmp`

Converts a palette file from quake (found in `id1/PAK0.pak/gfx`) to a PNG image representation of the palette


`python qpalconvert.py palette.png`

Converts a 16x16 image file into a quake palette lump.


To use the new palette in your mod, place it in your mod folder at `your_mod/gfx/palette.lmp`
