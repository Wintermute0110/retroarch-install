**Retroarch Install** is a set of scripts and utilities that allow easy compilation and configuration
of Retroarch. It has been tested in Debian and Ubuntu.

## Table of Contents

* **[Readme me first](#readme-me-first)**
* **[Cloning this repository](#cloning-this-repository)**
* **[Preparing Retroarch source code](#Preparing-Retroarch-source-code)**
* **[Compiling Retroarch](#Compiling-Retroarch)**
* **[Retroarch installation and configuration](#Retroarch-installation-and-configuration)**
* **[Updating Retroarch](#Updating-Retroarch)**
* **[Post installation notes](#Post-installation-notes)**

## Readme me first ##

In this tutorial it is assumed your username is `kodi` and your home directory `/home/kodi/`. 
The user name is only used to determine the paths. `~` always translate to your home directoy,
that is, `/home/kodi/`.

| Name                         | Path                                          |
|------------------------------|-----------------------------------------------|
| Home directory               | `/home/kodi/`                                 |
| Scripts directory            | `/home/kodi/Retroarch-Install/`               |
| Libretro directory           | `/home/kodi/bin/libretro/`                    |
| Retroarch data directory     | `/home/kodi/.retroarch`                       |
| Retroarch executable         | `/home/kodi/bin/retroarch`                    |
| Retroarch configuration file | `/home/kodi/.config/retroarch/retroarch.cfg/` |

Defaults can be edited in the file `path_configuration` (**not working at the moment, only the
defaults are valid**):
```
# File /home/kodi/Retroarch-Install/path_configuration
# No whitespaces in directory names.
# Add a trailing slash / at the end of directory names.
#
# WARNING: NOT WORKING AT THE MOMENT!
#
PATH_LIBRETRO=/home/kodi/bin/libretro/
PATH_RETROARCH_BIN=/home/kodi/bin/
PATH_RETROARCH_STUFF=~/.retroarch/
RETROARCH_CFG_FILE=~/.config/retroarch/retroarch.cfg
RETROARCH_CFG_DIR=~/.config/retroarch/
```

## Cloning this repository

Before you start make sure **git** is intalled on your machine. If you don't already have it, create
the directory `~/bin/` and cd into it. To clone this repository execute in:

```
git clone https://github.com/Wintermute0110/Retroarch-Install.git
```

This will create a directory named `~/bin/Retroarch-Install`.

## Preparing Retroarch source code

Go inside the directory `~/bin/Retroarch-Install` and execute

```
$ ./clone-libretro-super.sh
```

A new directory named `libretro-super` will be created inside `~/bin/Retroarch-Install`. 

### Compile Retroarch and the Libretro cores

This option is not recommended because the Libretro compiled cores can be downloaded with
the Retroarch **Online Core updater**, which saves a lot of time.

To customise the cores you want to download/compile, edit the file
`~/Retroarch-Install/libretro-super/build-config.sh` andd comment out the cores you don't want.
Note that if you don't customise the cores you want, the source code of all the available libretro
cores will be downloaded and compilation times may be very long. Some cores compile fast (about
a minute) but each MAME core can take as long as on hour in a fast machine.

### Compile only Retroarch

This is the preferred option. After the installation of Retroarch then you can download the
Libretro cores you want with the **Online Core updater**.

Edit the file `~/Retroarch-Install/libretro-super/libretro-fetch.sh` and comments the
following stuff at the end of the file:
```
# for a in $fetch_lutros; do
#       libretro_fetch "${a%%:*}"
# done

# for a in $fetch_devkits; do
#       libretro_fetch "${a%%:*}"
# done

# for a in $fetch_cores; do
#       libretro_fetch "${a%%:*}"
# done
```

### Download source code

Go to the directory `~/Retroarch-Install/` and execute `./update-retroarch.sh` This will download
the source code of both Retroarch and the cores you configured.

Then, as *root* user execute `./install-build-dependencies.sh` This will install the C/C++ compiler
and some other dependencies such as libraries required to compile Retroarch.

## Compiling Retroarch

Before compilation, go to the directory `~/Retroarch-Install/libretro-super/retroarch/` and
execute `git tag`. Each tag corresponds to a released version of Retroarch:
```
...
v1.7.4
v1.7.5
v1.7.6
```

Pick the version you want (usually the latest released version) and edit the file
`~/Retroarch-Install/compile-retroarch.sh`:
```
# --- Or switch to a specific release tag ---
git checkout tags/v1.7.6
```

To compile Retroarch, go to the directory  `~/Retroarch-Install/` and execute 
`./compile-retroarch.sh` to compile the Retroarch executable.

(OPTIONAL) If you didn't disable the Libretro cores, execute `./compile-libretro.sh` to compile
all the cores you selected to download.


## Retroarch installation and configuration

To install Retroarch, execute `./install-retroarch.sh` This will place the Retroarch executable
file in `~/bin/retroarch` and all the libretro cores in `~/bin/libretro/` (if you compiled them)
Also, it will create the directory `~/.retroarch` and copy all Retroarch assets, databases, etc.

To create a default Retroarch configuration file pointing to the correct directories, first
edit the file `~/Retroarch-Install/create-retroarch-default-config.py` and pick a default
configuration file:
```
# Configuration  --------------------------------------------------------------
# Configure paths to match your system (you can use ~ or absolute paths)
conf_source_path = '/home/kodi/Retroarch-Install/retroarch-1.7.6.cfg'
...
# Directory where you have your ROMs.
ROMs_dir = '/home/kodi/AEL-ROMs/'
```

Note that `Retroarch-Install` includes only a few default configuration files, usually for the
newer version of Retroarch.

Finally, execute `./create-retroarch-default-config.py` to create the Retroarch configuration
file `~/.config/retroarch/retraoarch.cfg`. The configuration file is automatically edited
so all paths will point to the correct places in `~/.retroarch/`

A backup of the original configuration file is created in `~/.config/retroarch/retroarch_initial.cfg`. 
To see the changes between both files, go to `~/.config/retroarch/` and execute
`diff -u --color retroarch_initial.cfg retroarch.cfg`

## Updating Retroarch

Go to directory `~/Retroarch-Install/` and execute the following steps:

```
./update-libretro-super-using-git.sh
./update-retroarch.sh
git -C libretro-super/retroarch/ tag
nano compile-retroarch.sh
./compile-retroarch.sh
./install-retroarch.sh
nano create-retroarch-default-config.py
./create-retroarch-default-config.py
```

`nano` is the editor I use but feel free to use any other one such as `vim` or `emacs`.

## Post installation notes

1) The **System directory** is located in `~/.retroarch/system/` Here you have to put BIOS
files for the cores that require them.

2) The option `sort_savefiles_enable` is activated. Your saved games will be stored 
in `~/.retroarch/savefiles/core_name/rom_name`.

## Internal notes

### Creating a new Retroarch default configuration file

After a clean Retroarch installation, delete `~/.config/retroarch/retraoarch.cfg` and then 
execute `~/bin/retroarch`. This will create a default configuration file. Copy this file
with a name like `~/Retroarch-Install/retroarch-1.7.6.cfg` matching the Retroarch version.

### PPSSPP core assets

Write me.

### Dolphin core assets

Write me.
