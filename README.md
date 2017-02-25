**Retroarch Install** is a set of scripts and utilities that allow easy compilation and configuration
of Retroarch. It has been tested in Debian and Ubuntu.

## RetroArch installation steps ##

In this tutorial it is assumed your username is `kodi` and your home directory `/home/kodi/`. `~` means 
your home directoy, that is, `/home/kodi/`.

### Clone this repository in your machine

Before you start make sure **git** is intalled on your machine. If you don't already have it, create
the directory `~/bin/` and cd into it. To clone this repository execute in:

```
git clone https://github.com/Wintermute0110/RetroarchInstall.git
```

This will create a directory named `/home/kodi/bin/RetroarchInstall`.

### Download the `libretro-super` repository and customize your libretro cores

Go inside the directory `~/bin/RetroarchInstall` and execute

```
git clone https://github.com/libretro/libretro-super.git
```

A new directory named `libretro-super` will be created inside `~/bin/RetroarchInstall` Note that if you don't
customise the cores you want all the available libretro cores will be downloaded and installed and compilation
times may be very long. To customise the cores you want to download/compile, edit the file
```
~/RetroarchInstall/libretro-super/build-config.sh
```
and comment out the cores you don't want.
 
### Download the source and compile

In directory `~/bin/RetroarchInstall/` execute `./update-retroarch` This will download the source code of
both Retroarch and the cores you configured.

Then, as *root* user execute `./install-build-dependencies` This will install the C/C++ compiler and some
other dependencies such as libraries required to compilet Retroarch.

To compile Retroarch execute `./compile-retroarch` After this finishes, execute `./compile-libretro` to
compile all the cores you selected to download.

### Retroarch installation and configuration

To install Retroarch, execute `./install-retroarch` This will place the Retroarch executable file in
`/home/kodi/bin/retroarch` and all the libretro cores in `/home/kodi/bin/` Also, it will create the
directory `~/.retroarch` and copy all Retroarch assets, databases, etc. in there.

Finally, execute `./create-retroarch-default-config.py` to create the Retroarch configuration
file `~/.config/retroarch/retraoarch.cfg`. The configuration file is automatically edited so all paths
will point to the correct places.

### Post installation notes

1) The **System directory** is located in `~/.retroarch/system/` Here you have to put BIOS files for the
cores that require them.

2) The option `sort_savefiles_enable` is activated. Your saved games will be stored in `~/.retroarch/savefiles/core_name/rom_name`.
