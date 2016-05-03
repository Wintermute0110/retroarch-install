# Retroarch Install #

**Retroarch Install** is a set of scripts to easily compile and install RetroArch/Libretro
under Linux. Tested in Debian and Ubuntu.

## RetroArch installation steps ##

1. Execute `./clone-libretro-super`

2. Edit libretro-super/xxxx to select the cores you want

3. Execute `./update-retroarch`

4. Execute as root `./install-build-dependencies`

5. Execute `./compile-libretro`

6. Execute `./compile-retroarch`

7. Execute `./install-retroarch`

8. Execute `./create-retroarch-default-config.py`

You will have RetroArch binary installed in `~/bin/bin-retroarch` and RetroArch
files and assets in `~/.retroarch/`.

Retroarch configuration file placed in default location `~/.config/retroarch/retraoarch.cfg`
and all directories and paths should be correctly created and configured. In particular,

1. System directory is `~/.retroarch/system/`. Here you have to put BIOS files.

2. If PPSSPP core is compiled xxxx
